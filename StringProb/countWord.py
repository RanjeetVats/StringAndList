name=input("enter the string")
count=1
i=0
l=len(name)-1
while(i<l):
    if(name[i]==" " and name[i-1]!=" "):
        count+=1
    i+=1
print("no of words:", count)