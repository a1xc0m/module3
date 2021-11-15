def area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c))**0.5
    return s

x = float(input('Введите значение X: '))
y = float(input('Введите значение Y: '))
z = float(input('Введите значение Z: '))
print(area(x, y, z))