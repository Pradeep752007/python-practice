# Menu-driven program to perform basic arithmetic operations using conditional statements
a=int(input("Enter the value of the first number: "))
b=int(input("Enter the value of the second number: "))
print("                MAIN MENU LIST\n               ")
print("1.ADDITION OF TWO NUMBERS")
print("2.SUBTRACTION OF TWO NUMBERS")
print("3.MULTIPLICATION OF TWO NUMBERS")
print("4.DIVISION OF TWO NUMBERS")
print("5.EXIT")
choice=int(input("Enter your choice:"))
if choice==1:
    x=a+b
    print("ADDITION OF THE GIVEN TWO NUMBERS GIVES:",x)
if choice==2:
    if a>b:
        y=a-b
        print("SUBTRACTION OF THE GIVEN TWO NUMBERS GIVES:",y)
    else:
        y=b-a
        print("SUBTRACTION OF THE GIVEN TWO NUMBERS GIVES:",y)
if choice==3:
    z=a*b
    print("PRODUCT OF THE GIVEN TWO NUMBERS GIVES:",z)
elif choice==4:
    if b==0:
        print("Division is not possible")
    else:
        d=a/b
        print("DIVISION OF THE GIVEN TWO NUMBERS GIVES:",d)
elif choice==5:
    print("Oops! IT SEEMS THAT YOU AREN'T INTERESTED IN PERFORMING ANY ARITHMETICE OPERATION")
    
print("Thank you for using the menu driven program for performing arithmetic operations!!")
