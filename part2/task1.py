a = [1, 2, 3, 'e', 'a', 3, 13, 77, 'qwerty']
b = []

for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
        
print(b)
