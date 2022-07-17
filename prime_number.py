n=int(input("Enter the number= "))
i=1
count=0
while(i<=n):
    i=i+1
    if(n%i==0):
        count=count+1
 #for while loop
if(count==2):
    print("Prime number")
else:
    print("Not prime ")     