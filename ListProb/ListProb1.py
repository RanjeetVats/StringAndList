list = ['larry', 'curly', 'moe']
list.append('shemp')
list.insert(0, 'xxx')
list.extend(['yyy', 'zzz'])
print(list)
index=list.index('curly')
print(index)

list.remove('curly')
print(list)

list.pop(1)
print(list)
list.sort()
print(list)
