# c = False
# if c:
#     print('Правда')
# else:
#     print('Ложь')

# c = 1
# if c == 1:
#     print('Один')
# if c == 2:
#     print('Два')
# if c == 3:
#     print('Три')


# А теперь смотрим с помощью дебага, что будет, если не if, а elif

# c = 1
# if c == 1:
#     print('Один')
# elif c == 2:
#     print('Два')
# elif c == 3:
#     print('Три')
# Видим, что программа как только выполняется условия завершается


# Простой разор цикла while
# num = 55
# count = 0
# while count < 7:
#     count += 1
#     print(num) # можем вывести сам count - print(count)

# Применение break или continue

# num = 77
# count = 0
# while count < 5:
#     count += 1
#     if count == 3:
#         break # Или continue - тогда напечается на один цикл меньше
#     print(num)

# Форматирование строк

# Метод format
# type_error = "Wrong data"
# value_error = "Division by Zero"
#
# template = "During working I've got an error: {}, {}".format(type_error, value_error)
# print(template)

# Метод f - строки
# text_1 = "I'm text 1"
# text_2 = "I'm text 2"
#
# template = f'Выводим данным методом наши переменные напрямую: {text_1}, {text_2}'
# print(template)

