import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1, b1 = map(float, input("Введите катеты первого треугольника (a1, b1): ").split())
a2, b2 = map(float, input("Введите катеты второго треугольника (a2, b2): ").split())

hypotenuse1 = calculate_hypotenuse(a1, b1)
hypotenuse2 = calculate_hypotenuse(a2, b2)

print(f"Гипотенуза первого треугольника: {hypotenuse1}")
print(f"Гипотенуза второго треугольника: {hypotenuse2}")

if hypotenuse1 > hypotenuse2:
    print("Гипотенуза первого треугольника больше.")
elif hypotenuse1 < hypotenuse2:
    print("Гипотенуза второго треугольника больше.")
else:
    print("Гипотенузы равны.")