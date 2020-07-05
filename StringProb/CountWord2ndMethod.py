#find Number of Occurrences of each Letter present in the given Strings
word=input("Enter any word: ")
l=word.split(" ")
count=0
d={}
for x in l:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    if v==1:
        count+=1
print(count)