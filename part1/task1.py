x = float(input('Введите сумму вклада: '))
p = float(input('Введите процент по вкладу: '))
y = float(input('Введите накопленную сумму вклада: '))

a = 0
while y > x:
    x = x + x * (p / 100)
    a = a + 1;
    
print(a)