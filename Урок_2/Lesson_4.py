#Пользователь вводит строку из нескольких слов, разделённых пробелами.
#Вывести каждое слово с новой строки.
#Строки необходимо пронумеровать.
#Если в слово длинное, выводить только первые 10 букв в слове.
my_str = input("введите строку ").split()
for index, i in enumerate(my_str):
    if len(str(my_str)) <= 10:
        print(f'#{index} - {i}')
    else:
        print(f'#{index} {i[0:10]}')