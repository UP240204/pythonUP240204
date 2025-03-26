#1. Write a code which gives grade to students according to theirs scores.
calif = int(input("Ingresa tu calificación del 0 al 100: "))
if calif >= 90 and calif <= 100:
    print("Tu nota es A")
elif calif >= 70 and calif <= 89:
    print("Tu nota es B")
elif calif >= 60 and calif <= 69:
    print("Tu nota es C")
elif calif >= 50 and calif <= 59:
    print("Tu nota es D")
elif calif >= 0 and calif <= 49:
    print("Tu nota es F")
else:
    print("Que pedo mijo, esa calificación no existe 🙄")

#2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer.
mes = str(input("Ingresa el mes del año en el que te encuentras: "))
if mes == 'Septiembre' or mes == 'Octubre' or mes == 'Noviembre':
    print("Estas en otoño")
elif mes == 'Diciembre' or mes == 'Enero' or mes == 'Febrero':
    print("Estas en invierno")
elif mes == 'Marzo' or mes == 'Abril' or mes == 'Mayo':
    print("Estas en primavera")
elif mes == 'Junio' or mes == 'Julio' or mes == 'Agosto':
    print("Estas en verano")
else:
    print("eh mijo, escriba bien el mes 🙄")

#3. The following list contains some fruits: If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list').
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input("Ingresa la fruta: "))
if fruit in fruits:
    print("Esa fruta ya existe en la lista 👍")
else:
    print("La lista de frutas es:",fruits)
    fruits.append(fruit)
    print("La nueva lista de frutas es:",fruits)