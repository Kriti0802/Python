# Python Program to Find Product of Digits

n=int(input("Enter the number: "))
prod=1
last=0
while(n>0):
    last=n%10
    prod*=last
    n=n//10
    
    print("prod= ",prod)