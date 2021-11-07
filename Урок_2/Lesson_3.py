#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.
my_list = ['Зима', 'Весна', 'Лето', 'Осень']
my_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'сень'}
i = int(input('Введите номер месяца: '))
if i == 1 or i == 12 or i == 2:
    print(my_dict.get(1))
    print(my_list[0])
elif i == 3 or i == 4 or i == 5:
    print(my_dict.get(2))
    print(my_list[1])
elif i == 6 or i == 7 or i == 8:
    print(my_dict.get(3))
    print(my_list[2])
elif i == 9 or i == 10 or i == 11:
    print(my_dict.get(4))
    print(my_list[3])
else:
    print("Такого месяца не существует")