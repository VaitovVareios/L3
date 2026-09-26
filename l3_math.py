import math
length = int(input("Пожалуйста введите радиус круга в (см): "))
print(f"{2*3.14*length} см. {(2*3.14*length)/100} м.- длина окружности, {3.14*(length**2)} см. {(3.14*(length**2))/100} м. - площадь круга")

print(f"{length*math.sqrt(2)} см., {(length*math.sqrt(2))/100} м. - сторона вписанного в окружность квадрата, {length*math.sqrt(3)} см. , {(length*math.sqrt(3))/100} м. - сторона равностороннего треугольника")

print(f"{2*length} см. , {(2*length)/100} м. - сторона квадрата. {2*math.sqrt(3)*length} см., {(length*2*math.sqrt(3))/100}  м. - cторона равностороннего треугольника. {2*(math.sqrt(2)-1)*length} см., {(2*(math.sqrt(2)-1)*length)/100} м. - сторона восьмиугольника")