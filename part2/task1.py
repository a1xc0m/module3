list = [1, 2, 3, 'e', 'a', 3, 13, 77, 'qwerty']
a = []

for x in range(len(list)):
    if list[x] not in a:
        a.append(list[x])
        
print(a)
