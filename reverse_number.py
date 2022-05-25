n=int(input("Enter the number: "))
last=0
rev=0

while n>0:
    last=n%10
    print("last= ",last)
    rev=(rev*10)+last
    print("rev= ",rev)
    n=n//10
    print("rev1= ",rev)