books=[]
issued_books=[]
def add_book():
    name=input("enter the name of the book:")
    books.append(name)
    print(name,"is added")
def show_books():
    if len(books)==0:
        print("no books avaliable")
    else:
        print("avaliable books:")
        for b in books:
                print(b)
def borrow_books():
     name=input("Enter the book you want to barrow:")
     if name in books:
        issued_books.append(name)
        books.remove(name)
        print(name,"is issued")
     else:
          print(name,"is not issued")
def return_books():
     name=input("Enter the name of the book:")
     if name in issued_books:
          issued_books.remove(name)
          books.append(name)
          print(name,"is returned")
     else:
          print(name,"is not issued")
def library():
     while True:
            print('menu')
            print('1.Add book')
            print('2.Show books')
            print('3.Borrow books')
            print('4.Return books')
            print('5.Exit')
            choice = int(input('Enter the choice:'))
            if choice == 1:
                 add_book()
            elif choice == 2:
                 show_books()
            elif choice==3:
                 borrow_books()
            elif choice==4:
                 return_books()
            elif choice==5:
                 print("Thank you!!vist Again")
                 break
            else:
                 print('invalid choice')
library()
