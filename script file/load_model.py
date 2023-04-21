import torch
import torchvision
import torchvision.utils

import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
from torchvision import transforms
import torch.optim as optim
  
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, Dataset ,SubsetRandomSampler
from torch.autograd import Variable

from torch.optim import lr_scheduler
from torch.cuda import amp


import os
import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import Image
import PIL.ImageOps  

import gc
import cv2
import copy
import time
import random

# Utils
import joblib
from tqdm import tqdm
from collections import defaultdict

# For Image Models
import timm

# Albumentations for augmentations
import albumentations as A
from albumentations.pytorch import ToTensorV2

# For descriptive error messages
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


class RealEstateModel(nn.Module):
    def __init__(self, model_name,embedding_size, pretrained=True):
        super(RealEstateModel, self).__init__()
        self.model = timm.create_model(model_name, pretrained=pretrained, num_classes=0)
        self.fc = nn.LazyLinear(embedding_size)
        self.dropout = nn.Dropout(p=0.3)

    def forward(self, images):
        features = self.model(images)
        features = self.dropout(features)
        output = self.fc(features)
        return output

def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    CONFIG = checkpoint['CONFIG']
    load_model = RealEstateModel(CONFIG['model_name'],CONFIG['embedding_size'])
    load_model.load_state_dict(checkpoint['state_dict'])
    
    return load_model