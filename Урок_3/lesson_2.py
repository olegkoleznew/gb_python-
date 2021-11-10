# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def my_param (name, surname, year, city, email, tel):
    print(name, surname, year, city, email, tel)


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город: ')
email = input('Введите эл.почту: ')
telephone = input('Введите тел.: ')
my_param(name=name, surname=surname, year=year, city=city, email=email, tel=telephone)
