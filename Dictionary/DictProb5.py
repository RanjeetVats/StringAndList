#Count frequency of word
s=input("Enter string")
l=s.split()
d={}
for i in l:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
print(d)
