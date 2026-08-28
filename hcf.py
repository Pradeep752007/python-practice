#Program to find the HCF of the two numbers
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
hcf=1
if a>b:
  num=b
else:
  num=a
for i in range(1,num+1): # Here num takes the value of the smaller of the two numbers
  if a%i==0 and b%i==0: #smaller number is taken because HCF can never be greater than the smaller number
    hcf=i
print("The HCF of the given two numbers ",a," and ",b," is: ",hcf)
