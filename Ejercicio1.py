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
print("El área es de:",area,"unidades cuadradas")
