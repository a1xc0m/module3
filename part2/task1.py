l = [1, 2, 3, 'e', 'a', 3, 13, 77, 'qwerty']
a = []

for x in range(len(l)):
    if l[x] not in a:
        a.append(l[x])
        
print(a)
