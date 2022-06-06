str=input("enter string= ")
print("reverse= ",str[::-1])


# and like this also

a=input("enter string= ")
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")