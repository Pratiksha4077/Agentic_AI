Library={}

while True:
    print("\n1.Add Book \n2.View Book \n3.Search Book \n4.Delete Book \n5.Exit")
    ch=int(input("Enter your choice :"))

    match ch:
        case 1:
            name=input("Enter Name of Book :")
            author=input("Enter author name :")
            Library[name]=author
            print("Add Book Successfully")

        case 2:
            for i in Library.items():
                print(i)
            print("View Books successfully")

        case 3:
            nm=input("Enter Name to search :")
            for i in Library.items():
                if nm==i[0]:
                    print(i)
                    print("search book is successful")
                    break
            else:
                print("Not Found")
        
        case 4:
            name=input("Enter Name to delete:")
            for i in Library.items():
                if name==i[0]:
                    del Library[name]
                    print("Delete Book Successfully")
                    break
            else:
                print("Not found this name")

        case 5:
            exit()
            
            