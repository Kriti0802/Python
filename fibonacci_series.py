
n=int(input("Enter the no. "))
x=0
y=1
z=0
while(z<=n):
    print("z= ",z)
    x=y
    y=z
    z=x+y
    
print("Series sum is= ",z)