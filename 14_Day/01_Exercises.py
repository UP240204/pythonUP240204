#1. Explain the difference between map, filter, and reduce.
#-map() se usa cuando queremos transformar todos los elementos de una lista.
#-filter() se usa cuando queremos seleccionar ciertos elementos de una lista.
#-reduce() se usa cuando queremos combinar todos los elementos en un único resultado.

#2. Explain the difference between higher order function, closure and decorator.
#Una función de orden superior es aquella que recibe una función como argumento o devulve una función como resultado.
#Un cierre es una función anidada que recuerda las variables del ámbito externo aunque ese ámbito haya terminado.
#Un decorador es una función especial que modifica el comportamiento de otra función sin cambiar su código.

#3. Define a call function before map, filter or reduce, see examples.
from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print(total)

#4. Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

#5. Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

#6. Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)