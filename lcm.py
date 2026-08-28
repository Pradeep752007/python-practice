#Program to calculate the LCM of any two numbers
first=int(input("Enter the first number: "))
second=int(input("Enter the second number: "))
if first>second:
    for i in range(1,second+1):#Using Iterative approach to calculate lcm
        s=first*i # Calculate the current multiple of the first number
        if s%second==0: # Check whether this multiple is also divisible by the second number
            break       # If it is divisible, we have found the LCM
    print("The LCM of ",first," and ",second," is: ",s)
elif first==second:
    print("The LCM of ",first," and ",second," is: ",first)
else:
    for i in range(1,first+1):
        p=second*i
        if p%first==0:
            break
    print("The LCM of ",first," and ",second," is: ",p)
