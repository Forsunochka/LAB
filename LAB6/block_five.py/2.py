def fibonacci(k):
    if k == 1 or k == 2:
        return 1
    return fibonacci(k - 1) + fibonacci(k - 2)

# Ввод значения k
k = int(input("Введите номер члена последовательности Фибоначчи (k): "))
result = fibonacci(k)
print(f"{k}-й член последовательности Фибоначчи: {result}")