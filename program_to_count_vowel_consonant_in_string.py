# Python Program To Count Vowels and Consonant in Given String in Python

str=input("enter string= ")
vowel=0
cons=0
print("length= ",len(str))
for i in range(0,len(str)):
 if(str[i]!=' '):
    if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' or str=='A' or 
       str[i]=='E' or str[i]=='I' or str[i]=='O' or str[i]=='U'):
    
     vowel=vowel+1
    
    else:
      cons=cons+1

print("vowel= ",vowel)
print("consonant= ",cons)
