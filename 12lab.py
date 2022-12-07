#1
#В приведенной ниже программе показаны дополнительные примеры способов чтения и записи данных в текстовый файл. Каждая строка кода имеет комментарии, которые помогут вам понять, что происходит:
# Программа, показывающая различные способы чтения и
# записать данные в текстовый файл.

file = open("myfile.txt","w")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]

#я назначил ["This is Lagos \n","This is Python \n","This is Fcc \n"] к переменной L

  
#\n ставится для обозначения конца строки

file.write("Hello There \n")
file.writelines(L)
file.close()
# используйте close() для изменения режима доступа к файлу

file = open("myfile.txt","r+") 
print("Output of the Read function is ")
print(file.read())
print()
  
# seek(n) переводит дескриптор файла на n-й
#байт с самого начала.
file.seek(0) 
  
print( "The output of the Readline function is ")
print(file.readline()) 
print()
  
file.seek(0)
  
# Чтобы показать разницу между read и readline

print("Output of Read(12) function is ") 
print(file.read(12))
print()

file.seek(0)
  
print("Output of Readline(8) function is ") 
print(file.readline(8))
  
file.seek(0)
# readlines function
print("Output of Readlines function is ") 
print(file.readlines()) 
print()
file.close()

Приведенный выше код показывает, что функция «readline()» возвращает букву на основе указанного для нее числа, а функция «readlines()» возвращает каждую строку, назначенную «L», включая \n. То есть функция «readlines()» распечатает все данные в файле.



#2
my_file = open("test.txt", mode="w+")
print("Как называется файл?", my_file.name)
print("Каков режим файла?" , my_file.mode)
print("Какой формат кодирования?", my_file.encoding)
 
text = ["Hello Python\n", "Good Morning\n", "Good Bye"]
my_file.writelines(text)
 
print("Размер файла:", my_file.__sizeof__())
print("Позиция курсора в байте:", my_file.tell())
my_file.seek(0)
print("Содержимое файла:", my_file.read())
my_file.close()
 
file = open("test.txt", mode="r")
 
line_number = 3
current_line = 1
data = 0
for line in file:
	if current_line == line_number:
		data = line
		print("Данные, присутствующие в текущей строке:", data)
		break
	current_line = current_line + 1
 
bin_file = open("bfile.exe", mode="wb+")
message_content = data.encode("utf-32")
bin_file.write(message_content)
bin_file.seek(0)
bdata = bin_file.read()
print("Двоичные данные:", bdata)
ndata = bdata.decode("utf-32")
print("Нормальные данные:", ndata)
file.close()
bin_file.close()



#3
# Запись/чтение двумерной матрицы чисел
#Исходная матрица целых чисел размером 3*4
M = [ [ 2, 1, -3],
      [ 4, 8, -2],
      [ 1, 2,  3],
      [ 7, -3, 8] ]

#Запись матрицы в текстовый файл

#Открыть текстовый файл для записи
f = open('myfile8.txt', 'w')

#Цикл записи элементов матрицы в файл
#в удобном для отображения виде
i = 0
while i < 4: # цикл по строкам
    j = 0
    while j < 3: # цикл по столбцам
        s = str(M[i][j])
        f.write(s + ' ') # между числами символ ' ' пробел
        j = j+1
    f.write('\n')
    i = i + 1

# Закрыть файл
f.close()

# Чтение матрицы из файла
# Открыть файл для чтения
f = open('myfile8.txt', 'rt')

# Создать пустой список
M2 = []

#Чтение данных из файла и образование новой матрицы

i = 0
for line in f: # Использовать итератор файла
    # Конвертировать строку line в список строк
    lines = line.split(' ') # разбить строку line на подстроки lines

    # временный список
    lst = []

    # обход элементов в строке
    for ln in lines:
        # забрать символ '\n'
        ln = ln.rstrip()

        if ln != '':
            num = int(ln) # взять отдельное число
            lst = lst + [num] # добавить число к списку

    M2 = M2 + [lst] # добавить строку к результирующей матрице

#Вывести матрицу M2 для контроля
print("M2 = ", M2) #

#Закрыть файл
f.close()


#4
# Запись/чтение данных разных типов.
# Обработка списка и кортежа.
#Задан некоторый список строк и кортеж чисел
L = [ 'John Johnson', 'Peter Petrov', 'O Neill', 'J. Dunkan' ]
T = ( 2, 3.85, 7.77, -1.8, 5.25 )

#Запись данных в файл: сначала записывается список, затем кортеж
#Открыть текстовый файл для записи
f = open('myfile9.txt', 'w')

#Записать количество элементов списка + '\n'
f.write(str(len(L)) + '\n')

#Цикл записи элементов списка в файл
# Каждый из элементов списка размещается в новой строке.
for item in L: # обход списка
    f.write(item + '\n') # записать строку в файл

# После списка записывается кортеж,
# каждый элемент кортежа размещается в отдельной строке.
# Сначала записать количество элементов кортежа
f.write(str(len(T)) + '\n')

# обход кортежа в цикле
for item in T:
    f.write(str(item) + '\n') # запись каждого элемента кортежа

#Закрыть файл
f.close()

#Чтение списка и кортежа из файла
# Открыть файл для чтения
f = open('myfile9.txt', 'rt')

#Создать результирующий пустой список
# и результирующий кортеж
L2 = []
T2 = ()

#Чтение данных из файла и формирование списка L2
n = int(f.readline()) # прочитать количество элементов в списке

i = 0
while i < n: # цикл чтения строк из файла и образования списка
    s = f.readline().rstrip() # прочитать строку без символа '\n'
    if (s != ''):
        L2 += [s]
    i = i + 1

# Прочитать количество элементов кортежа
n = int(f.readline())

i = 0
while i < n: # цикл чтения строк и образование кортежа
    s = f.readline()
    if (s != ''):
        T2 = T2 + (float(s),) # добавить вещественное число к кортежу
    i = i+1

#Закрыть файл
f.close()

# Вывести список и кортеж для контроля
print("L2 = ", L2)
print("T2 = ", T2)