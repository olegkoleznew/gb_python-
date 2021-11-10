# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(num_1, num_2, num_3):
    if num_1 > num_3 and num_2 > num_3:
        return num_1 + num_2
    elif num_1 > num_2 and num_2 < num_3:
        return num_1 + num_3
    else:
        return num_2 + num_3


a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
print(my_func(a,b,c))