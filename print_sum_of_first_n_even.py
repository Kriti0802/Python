# Python Program to find Sum of First N Even Numbers 

n=int(input("Enter the number= "))
i=1
count=0  #this count is for counting <n
sum=0

while(count<n):
    if(i%2==0):
        sum=sum+i
        count=count+1
    i=i+1  #this increment is for while loop
    print("sum is= ",sum)

#example
#n=3
#count=0 o<3
#check for even not then increment
#if even the sum and count increment


