a = int(input("Введите значение a (0<=a<=50)"))

if 0<=a<=50:
    squart=0
    for i in range (a,51):
        squart +=i**2
        
       
else:
        print ("Введено неправильное значение a!!!")     
        
print ("Сумма квадратов всех чисел от ", a, " до 50: ", squart)   