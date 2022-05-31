# Python Program to Check a Number is Palindrome or Not 

n=int(input("Enter the number: "))
num=n
rev=0
last=0
while n>0:
    last=n%10
    rev=(rev*10)+last
    n=n//10
    
    if(num==rev):
        print("palindrome number")
    else:
        print("not palindrome")
    