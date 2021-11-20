# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
myfile = open('file.txt', 'r')
content = myfile.read()
print("Содержимое файла : \n", content)

myfile = open('file.txt', 'r')
content = myfile.readlines()
print("Количество строк в файле :", len(content))

myfile = open('file.txt', 'r')
i = 1
for line in  myfile.readlines():
    i += 1
    print("Количество слов в ", i - 1, "строке равно :", len(line.split(' ')))

myfile.close()
