age = [22, 19, 24, 25, 26, 24, 25, 24]

#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?.
age_set = set(age)
print("Lista:",age)
print("Conjunto:",age_set)
if len(age) == len(age_set):
    print("La longitud de la lista es igual a la del conjunto")
elif len(age) > len(age_set):
    print("La longitud de la lista es mayor que la del conjunto")
else:
    print("La longitud del conjunto es mayor que la de la lista")

#2. Explain the difference between the following data types: string, list, tuple and set.
    #El 'string' se escibe entre comillas o apostrofes, y se utiliza cuando se trabaja con datos de texto.
    #El 'list' se define entre corchetes, y se utiliza cuando se necesita una colección ordenada y modificable.
    #El 'tuple' se define entre parentesis, y se utiliza cuando se necesita una colección ordenada pero inmutable.
    #El 'set' se definde entre corchetes, y se utiliza cuando se necesita una colección de elementos únicos sin preocuparte por el orden.

#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
print("Las palabras unicas de la oración son:",sentence.split())


print("Revisado")