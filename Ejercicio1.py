#1. Declare your age as integer variable
age = 18
print(type(age))

#2. Declare your height as a float variable
height = 79.5
print(type(height))

#3. Declare a variable that store a complex number
complejo = 3+8j
print(type(complejo)) 

#4. Write a script that prompts the user to enter base 
# and height of the triangle and calculate an area of 
# this triangle (area = 0.5 x b x h).
base = float(input("Ingresa el valor de la base: "))
altura = float(input("Ingresa el valor de la altura: "))
area = 0.5 * base * altura
print("El área del triangulo es de",area,"unidades cuadradas")

#5. Write a script that prompts the user to enter side a, 
# side b, and side c of the triangle. Calculate the perimeter 
# of the triangle (perimeter = a + b + c).
side_a = float(input("Ingresa el valor del primer lado: "))
side_b = float(input("Ingresa el valor del segundo lado: "))
side_c = float(input("Ingresa el valor del tercer lado: "))
perimeter = side_a + side_b + side_c
print("El perimetro del triangulo es de",perimeter,"unidades")

#6. Get length and width of a rectangle using prompt. Calculate 
# its area (area = length x width) and perimeter (perimeter = 2 x (length + width)).
length = float(input("Ingresa el largo del rectangulo: "))
width = float(input("Ingresa el ancho del rectangulo: "))
a = length * width
perimetro = 2*(length + width)
print("El area del rectangulo es de",a,"unidades cuadradas y su perimetro es de",perimetro,"unidades")

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) 
# and circumference (c = 2 x pi x r) where pi = 3.14.
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
word_1 = "python"
word_2 = "dragon"
length_1 = len("python")
length_2 = len("dragon")
print("La longitud de",word_1,"es",length_1)
print("La longitud de",word_2,"es",length_2)
comparación = bool(length_1>length_2)
print("¿La palabra 'python' es más larga que 'dragon'?",comparación)

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'.
in_word_1 = bool("on" in word_1)
in_word_2 = bool("on" in word_2)
both_words = in_word_1 and in_word_2
print("¿El 'on' esta en ambas palabras?",both_words)

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.