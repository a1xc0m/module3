s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто граций серого.
Так всегда первого ноль девятого
То ли весь мир сошел с умаБ то ли я - того...
На столе записка от неё смятая
Недопитый виски допивая с матами.
Посмотрю в окно, допишу главу
Первое сентбря, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''


def decompose(str):
    print('Разбиваем строку на список. Разделяем строку посимвольно, игорируя пробелы')
    string = list(str.split(' '))
    print('Создаем пустую переменную список')
    str1 = []
    print('Создаем переменную, где хранятся специальные символы ? ! - , .')
    str2 = ['\n', '.', ',', '!', '?', '-']
    print('Запускаем цикл. Перебор строки. Если длинна символов менее 5 (до ближайшего пробела) и строка не содержит специальный символ, добовляем его в переменную')
    for i in range(len(string)):
        if (len(string[i]) < 5) and (string[i] not in str2):
            str1.append(string[i])
    print(str1)


decompose(s)