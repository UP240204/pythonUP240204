#1. Iterate 0 to 10 using for loop, do the same using while loop.
i = 0
while i < 11:
    print(i)
    i = i + 1 

#2. Iterate 10 to 0 using for loop, do the same using while loop.
a = 10
while a > -1:
    print(a)
    a = a -1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle.
for i in range(8):
    print("#"*i)

#4. Use nested loops to create the following.
for c in range(8):
    print("#"*8)

#5. Print the following pattern.
operacion = 0
while operacion < 11:
    print('{} X {} = {}'.format(operacion,operacion,operacion*operacion))
    operacion = operacion + 1 

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills:
    print(skill)

#7. Use for loop to iterate from 0 to 100 and print only even numbers.
numero = 0 
for numero in range(101):
    if numero % 2 == 0:
        print(numero)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers.
number = 1
while number < 101:
    print(number)
    number = number + 2 