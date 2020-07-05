value=input("enter string")
l=value.split()
d={}
for i in l:
    d[i]=d.get(i, 0)+1
print(d)


