# Ввод трех целых чисел
numbers = input("Введите три целых числа, разделенные пробелом: ").split()

# Преобразуем введенные данные в целые числа
numbers = list(map(int, numbers))

# Фильтруем числа, которые принадлежат интервалу [1, 3]
filtered_numbers = [num for num in numbers if 1 <= num <= 3]

# Выводим результат
print("Числа в интервале [1, 3]:", filtered_numbers)