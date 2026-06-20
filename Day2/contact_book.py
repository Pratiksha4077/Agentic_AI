contact={}

while True:
    print("\n1.Add contact \n2.View Contacts \n3.Search Contact \n4.Delete Contact \n5.Exit")
    ch=int(input("Enter your choice :"))

    match ch:
        case 1:
            name=input("Enter Name :")
            ph_no=int(input("Enter Phone no. :"))
            contact[name]=ph_no
            print("Add contact Successfully")

        case 2:
            for i in contact.items():
                print(i)
            print("View successfully")

        case 3:
            nm=input("Enter Name to search :")
            for i in contact.items():
                if nm==i[0]:
                    print(i)
                    print("search is successful")
                    break
            else:
                print("Not Found")
        
        case 4:
            name=input("Enter Name to delete:")
            for i in contact.items():
                if name==i[0]:
                    del contact[name]
                    print("Delete Successfully")
                    break
            else:
                print("Not found this name")

        case 5:
            exit()
            
            