#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
number = 0
for a in range(101):
    print(number)
    number = number + a
print("La suma de los numeros del 0 al 100 es",number)

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
numpar = []
numimpar = []
for b in range(101):
    if b % 2 == 0:
        numpar.append(b)
    else:
        numimpar.append(b)
print("Los numeros pares del 0 al 100 son:",numpar)
print("La suma de estos numeros pares es",sum(numpar))
print("Los numeros impares del 0 al 100 son:",numimpar)
print("La suma de estos numeros impares es",sum(numimpar))