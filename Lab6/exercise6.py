"""
student Name:jatuphon chit
ID :021
Group :mit211
"""

"""
จงเขียนโปรแกรมรับค่าข้อมูลหนังสือ ประกอบด้วย ชื่อหนังสือ ราคา ผู้แต่ง สำนักพิมพ์ 
โดยการถามผู้ใช้ว่า มีหนังสือกี่เล่ม จากนั้นให้รับค่าข้อมูลดังกว่าว และเก็บข้อมูลไว้ใน object จากนั้นเก็บ
object ไว้ใน list ชื่อ mybook_store แสดงผลข้อมูลหนังสือทั้งหมดทางหน้าจอภาพ

ัตัวอย่างนำเข้าข้อมูล เช่น
คุณมีหนังสือท้ังหมดกี่เล่ม: 1 
ชื่อหนังสือ: OOP
ราคา: 200
ผู้แต่ง: ภูริวัฒน์ เลิศไกร
สำนักพิมพ์: MT

ตัวอย่างแสดงผล เช่น
Book name: OOP | Price: 200.0 THB | Auther: Puriwat Lertkrai | Publisher: MT Familly
"""




from book import Book

b3 = Book("GTA",200.00,"Jatuphon Chit","MIT")

mybook = [b3]
for x in mybook:
    print(x.book_detail())