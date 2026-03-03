# Program to compute the factorial of a given number using an iterative approach
# Handles negative numbers and zero as special cases
Num=int(input("Enter the value of a number :"))
Fact=1
if Num<0:
    print("Factorial does not exist for negative numbers")
elif Num==0:
    print("The factorial of ",Num,"which is represented in factorial terms as ",Num,"! is : 1")
else:
    for i in range(1,Num+1):
        Fact=Fact*i
    print("The factorial of ",Num,"which is represented in factorial terms as ",Num,"! is :",Fact)

# Print statement should be placed outside the loop
# Reason: Inside loop prints for every iteration(intermediate results) , outside loop prints only desired value (factorial value) i.e., value of the final iteration

