marks=int(input("Enter Marks :"))

if marks>85:
    print("Grade A+")
elif marks>75:
    print("Grade A")
elif marks>60:
    print("Grade B")
elif marks>50:
    print("Grade C")
elif marks>40:
    print("Pass")
else:
    print("Fail")