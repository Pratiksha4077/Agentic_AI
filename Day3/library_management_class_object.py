class Library:
    def __init__(self):
        self.name=input("Enter Name of Book :")
        self.author=input("Enter author name :")
        self.no_of_pages=int(input("Enter no. of pages :"))
        

li=[]

while True:
    print("\n1.Add Book \n2.View Book \n3.Search Book \n4.Delete Book \n5.Exit")
    ch=int(input("Enter your choice :"))

    match ch:
        case 1:
            b=Library()
            li.append(b)
            print("Book is added")

        case 2:
            for i in li:
                print("\nName of book :",i.name,"\nAuthor name is :",i.author,"\nNo. of pages :",i.no_of_pages)
            print("Display record sucessfully")
        
        case 3:
            name=input("Enter Name of Book :")

            for i in li:
                if name==i.name:
                    print("Name of Book :",i.name)
                    print("Author is :",i.author)
                    print("No. of Pages :",i.no_of_pages)

                    print("Search record sucessfully")
                    break
            else:
                print("Book is not found")
        
        case 4:
            name=input("Enter Name of Book :")
            for i in li:
                if name==i.name:
                    li.remove(i)
                    print("Delete Book Successfully")
                    break
            else:
                print("Not found")

        case 5:
            exit()


