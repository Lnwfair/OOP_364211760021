from vaccineted import vaccine

vaccine_store = []
num = int(input(':'))

for x in range(num):
    bookname = input('ชื่อหนังสือ:')
    price = float(input('ราคา:'))
    auther = input('ชื่อผู้แต่ง:')
    publisher = input('สำนักพิมพ์:')
    #1
    b = Book(bookname,price,auther,publisher)
    book_store.append(b)
    #2
    #book_store.append(Book(bookname,price,auther,publisher))

def display_book(book):
    print('จำนวนหนังสือทั้งหมด:',len(book))
    for x in book:
        x.book_detail()

display_book(book_store)


