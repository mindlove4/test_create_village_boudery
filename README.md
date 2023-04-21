# โค้ดนี้สำหรับการทดสอบ model ที่ได้เทรนมา โดยการ encode เป็น vector แล้ว เปรียบเทียบ similarity
## ผลลัพธ์อยู่ใน notebook/load and test model

ทดสอบในบริเวณเดียว  
หลักการ  
-กำหนด latitude longtitude  
-ดึงรูปจาก salem โดยกำหนดขอบเป็น latitude-0.0001 ถึง latitude+0.0001  , longtitude-0.0001 ถึง longtitude+0.0001 โดย 0.0001 คือ 11 เมตร เป็นภาพในเขต 22*22 ตารางเมตรรอบจุด lat long  
-นำรูปไป embed กับ model และ เทียบ similarity  

cut off similarity ของ หมู่บ้านเดียวกันหรือไม่ในโค้ดนี้คือ 0.8  

ทดสอบ 2 แบบคือทดสอบโดยเปรียบเทียบภาพเดียว กับ ทดสอบโดยเฉลี่ยกับ 4 ภาพข้างๆ (สามารถทดสอบมากกว่านี้ได้)  

สุดท้ายลอง plot boudery โดยใช้ dbscan และ convex hull  
ผลลัพธ์ดังใน notebook และ html  
