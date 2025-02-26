#1. Declare your age as integer variable
age = 18
print(type(age))

#2. Declare your height as a float variable
height = 79.5
print(type(height))

#3. Declare a variable that store a complex number
complejo = 3+8j
print(type(complejo)) 

#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Ingresa el valor de la base: "))
altura = float(input("Ingresa el valor de la altura: "))
area = 0.5 * base * altura
print("El área del triangulo es de",area,"unidades cuadradas")

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Ingresa el valor del primer lado: "))
side_b = float(input("Ingresa el valor del segundo lado: "))
side_c = float(input("Ingresa el valor del tercer lado: "))
perimeter = side_a + side_b + side_c
print("El perimetro del triangulo es de",perimeter,"unidades")

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)).
length = float(input("Ingresa el largo del rectangulo: "))
width = float(input("Ingresa el ancho del rectangulo: "))
a = length * width
perimetro = 2*(length + width)
print("El area del rectangulo es de",a,"unidades cuadradas y su perimetro es de",perimetro,"unidades")

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radio = float(input("Ingresa el radio del circulo: "))
pi = 3.14
area_cir = pi * radio * radio
perimeter_cir = 2 * pi *radio
print("El area del circulo es de",area_cir,"unidades cuadradas y su perimetro es de",perimeter_cir,"unidades")

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2.
m = 2
b = -2
x_intercept = -b / m
print("Pendiente (m):",m)
print("Intersección en Y (b):",b)
print("Intersección en X:",x_intercept)

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10).
import math
x_1 = 2
y_1 = 2
x_2 = 6
y_2 = 10
pendiente = ((y_2)-(y_1))/((x_2)-(x_1))
euclides = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
print("La pendiente es",pendiente)
print("La distancia de Euclidiana es de",euclides)

#10. Compare the slopes in tasks 8 and 9.
if m == pendiente:
    print("La pendientes son iguales")
elif m>pendiente:
    print("La primera pendiente es mayor")
else:
    print("La segunda pendiente es mayor")

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_valor = float(input("Ingresa un valor para X: "))
y_valor = (x_valor**2) + 6*x_valor + 9
print("De la ecuación y=(x**2)+6x+9 para que y sea",y_valor,"x tiene que ser",x_valor)

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("¿La palabra 'python' es más larga que 'dragon'?",len("python") > len("dragon"))

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'.
print("¿El 'on' esta en ambas palabras?","on" in "python" and "on" in "dragon")

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("¿La palabra 'jargon' esta en la oración 'I hope this course is not full of jargon'?","jargon" in "I hope this course is not full of jargon")

#15. There is no 'on' in both dragon and python.
print("¿El 'on' no esta en 'dragon' y 'python'?","on" not in "dragon" and "on" not in "python")

#16. Find the length of the text python and convert the value to float and convert it to string.
print(str(float(len("python"))))

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?.
numero = int(input("Ingresa un numero: "))
if numero % 2 == 0:
    print(numero,"es un numero par")
else:
    print(numero,"es un numero impar")

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
ea = 7//3 == int(2.7)
print("¿La division de 7 entre 3 es igual a 2.7?",ea)

#19. Check if type of '10' is equal to type of 10.
ae = type("10") == type(10)
print("¿El tipo de '10' es igual al tipo de 10?",ae)

#20. Check if int('9.8') is equal to 10.
nel = int(9.8) == 10
print("¿'9.8' es igual a 10?",nel)

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?.
horas = int(input("¿Cuantas horas se trabajaste en la semana? "))
tarifa = float(input("¿Cuanto cobras la hora? "))
salario = horas * tarifa
print("Tu pago semanal es de $",salario,"pesos mexicanos")

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years.