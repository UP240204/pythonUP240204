#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers (num1, num2):
    sum = num1 + num2
    return sum
print("Suma:",add_two_numbers(5,6))

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle (pi,radio):
    area = pi * radio * radio
    return area
print("Area del circulo:",area_of_circle(3.1416,20))

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums (*args):
    if not all(isinstance(arg, (int, float)) for arg in args):                      #Verifica si todos los argumentos son enteros o flotantes
        return "Error: Todos los argumentos deben ser numeros (int o float)."
    return sum(args)
print("La suma de los numeros es:",add_all_nums(1,2,3,4,5))

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit (celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
print("La temperatura en fahrenheit es:",convert_celsius_to_fahrenheit(10))

#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season (month):
    if month in ['Diciembre','Enero','Febrero']:
        season = 'Estas en invierno'
    elif month in ['Marzo','Abril','Mayo']:
        season = 'Estas en primavera'
    elif month in ['Junio','Julio','Agosto']:
        season = 'Estas en verano'
    elif month in ['Septiembre','Octubre','Noviembre']:
        season = 'Estas en otoño'
    else:
        print("eh mijo, escriba bien el mes 🙄")
    return season
print(check_season('Abril'))