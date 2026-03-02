#Program to generate the fibanacci series upto n terms using while loop iteration 
User_Input=int(input("Enter the number of terms:"))
index=0
first=1
second=1
while index<User_Input:
    if index<1:
        Num=0
    elif index<=2:
        Num=1
    else:
        Num=first+second
        first=second
        second=Num
    index=index+1
    print(Num)
    
