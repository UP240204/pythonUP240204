#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
a = int(input("Ingresa tu edad: "))
falta = 18 - a
if a == 18 or a > 18:
    print("Tienes edad suficiente para conducir")
else:
    print("Te faltan",falta,"años para poder conducir")

#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 18
b = int(input("Ingresa tu edad: "))
diferencia = abs(b-18)
if b > 18:
    print("Eres",diferencia,"años mayor que yo")
elif b == 18:
    print("Tenemos la misma edad")
else:
    print("Soy",diferencia,"años mayor que tu")

#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
one = float(input("Ingresa el primer numero: "))
two = float(input("Ingresa el segundo numero: "))
if one > two:
    print(one,"es mayor que",two)
elif one < two:
    print(one,"es menor que",two)
else:
    print(one,"es igual que",two)

print("Revisado")