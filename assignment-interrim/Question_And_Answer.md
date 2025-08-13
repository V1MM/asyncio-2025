# Question
1. ถ้าสร้าง asyncio.create_task(*tasks) ที่ไม่มี await ที่ main() เกิดอะไรบ้าง
   1. Task จะถูกสร้างและเริ่มรันทันที แต่ main() อาจจบการทำงานก่อน ทำให้ Task อาจยังรันไม่เสร็จหรือถูกยกเลิก
   2. ไม่มีการรอให้ Task เสร็จ จึงอาจไม่ได้ผลลัพธ์หรือเกิดการสูญเสียข้อมูลกลางทาง
   3. อาจมี ERROR แต่จะไม่ถูก raise ขึ้นมา ต้องมีการ handle code ที่เหมาะสม จึงสามารถดู ERROR ได้
2. ความแตกต่างระหว่าง asyncio.gather(*tasks) กับ asyncio.wait(tasks) คืออะไร
   1. gather คืนค่าผลลัพธ์ของทุก Task (เป็น list ตามลำดับที่ส่งเข้าไป) และถ้า Task ใด error จะ raise ขึ้นทันที
      wait คืนค่าเป็น tuple (done, pending) ของ set ของ Task และไม่คืนผลลัพธ์โดยตรง

   2. gather เหมาะสำหรับรอให้ทุก Task เสร็จและดึงค่าที่ return ได้
      wait เหมาะสำหรับรอเฉพาะบาง Task หรือรอตามเงื่อนไข เช่น return_when=FIRST_COMPLETED

   3. gather จะ cancel Task ที่เหลือเมื่อมี Task หนึ่ง error (โดย default)
      wait จะไม่ cancel Task อื่น ๆ ให้เอง ต้องจัดการเอง

3. สร้าง create_task() และ coroutine ของ http ให้อะไรต่างกัน
   1. ถ้าสร้าง coroutine ธรรมดา  จะยังไม่เริ่มรัน จนกว่าจะถูก await
   2. ถ้าใช้ create_task  จะได้ Task ที่เริ่มรันทันที และสามารถเก็บ reference ไปจัดการต่อได้
   3. Task จะถูกรันแบบ concurrent กับ Task อื่น ๆ ใน event loop ในขณะที่ coroutine ธรรมดาจะรอให้ถึงคิวของมันตอนถูก await เท่านั้น
