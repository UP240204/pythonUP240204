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

#6. Write a function called calculate_slope which return the slope of a linear equation.
def calculate_slope (x1,y1,x2,y2):
    m = (y2 - y1)/(x2 - x1)
    return m
print("La pendiente es:",calculate_slope(4,2,2,1))

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn (a,b,c):
    x1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)
    return x1,x2
print("Las soluciones son:",solve_quadratic_eqn(1,2,3))

#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list (lista):
    for elemento in lista:
        print(elemento)
print_list(['hagan','push','deaaaah'])

#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list (liston):
    reve_list = []
    for i in range(len(liston)-1,-1,-1):
        reve_list.append(liston[i])
    return reve_list
print(reverse_list([1,2,3,4,5]))

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items.
def capitalize_list_items (lista):
    return [elemento.upper() for elemento in lista]
liston = ['webos','python','chicharito']
print(capitalize_list_items(liston))

#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item (lista,item):
    lista.append(item)
    return lista
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Banana'))

#12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item (lista,item):
    lista.remove(item)
    return lista
numbers = [2, 3, 7, 9]
print(remove_item(numbers,7))

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers (number):
    sum = 0
    for i in range(1,number + 1):
        sum = sum + i
    return sum
print("La suma de los numeros del 1 al 5 es:",sum_of_numbers(5))
print("La suma de los numeros del 1 al 10 es:",sum_of_numbers(10))
print("La suma de los numeros del 1 al 100 es:",sum_of_numbers(100))

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds (number):
    return sum(i for i in range(number + 1) if i % 2 != 0) #si es diferente de cero
print("La suma de numeros impares del 1 al 9 es:",sum_of_odds(9))

#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even (number):
    return sum(i for i in range(number + 1) if i % 2 == 0)
print("La suma de numeros pares del 1 al 10 es:",sum_of_even(10))

print("Revisado")