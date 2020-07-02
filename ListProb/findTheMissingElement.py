l=[2,5,6,7,9]
h=max(l)
i=0
j=0
#print(h)
l2=[0]*h
#print(l2)
for i in l:
    l2.insert(i,1)
print(l2)

while j<=h:
    if l2[j]==0:
        print(j)
    j=j+1
