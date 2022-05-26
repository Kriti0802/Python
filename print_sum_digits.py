# Python Program to find Sum of Digits of a Given Number 

i=int(input("Enter the number= "))
# i=1
# sum=0
# while(i>0):
#    sum=sum+i%10
#    i=i//10
# print("sum= ",sum) 
    

    
   #  or
   
sum=0
last=0
while(i>0):
       last=i%10
       sum+=last
       i=i//10
print("sum= ",sum)
   
  
  
    
  
    
    
    
    
    
    
    
