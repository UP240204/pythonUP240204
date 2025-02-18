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