n1=int(input("Enter No1:"))
n2=int(input("Enter No2:"))

while True:

    print("1.Add\nn2.Substract\n3.Multiply\n4.Division")
    ch=int(input("Enter choice:"))

    match ch:
        case 1:
            print("Addition is :",n1+n2)
        
        case 2:
            print("Substarction is :",n1-n2)

        case 3:
            print("Multiplication is :",n1*n2)

        case 4:
            print("Division is :",n1//n2)

        