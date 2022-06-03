# Python Program to find Sum of Square of digits of a given Number 

n=int(input("Enter the number= "))
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)
    n=n//10
    print("sum = ",sum)