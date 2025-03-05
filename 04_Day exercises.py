#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word_1 = 'Thirty'
word_2 = 'Days'
word_3 = 'Of'
word_4 = 'Python'
space = ' '
full_sentence = word_1 + space + word_2 + space + word_3 + space + word_4
print(full_sentence)

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word_5 = 'Coding'
word_6 = 'For'
word_7 = 'All'
fulll_sentence = word_5 + space + word_6 + space + word_7
print(fulll_sentence)

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

#4. Print the variable company using print().
print(company)

#5. Print the length of the company string using len() method and print().
lenght = len(company)
print("La longitud de 'Coding For All' es de",lenght)

#6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9. Cut(slice) out the first word of Coding For All string.
print(company[7:14])

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print("¿'Coding For All' contiene 'Coding'?",'Coding' in company)

#11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))

#12. Change Python for Everyone to Python for All using the replace method or other methods.
chicharito = 'Python For All'
print(chicharito.replace('Python','Everyone'))

#13. Split the string 'Coding For All' using space as the separator (split()).
print(company.split())

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

#15. What is the character at index 0 in the string Coding For All.
print("El carácter en el índice 0 en la cadena 'Coding For All' es",company[0])

#16. What is the last index of the string Coding For All.
print("El último índice de la cadena 'Coding For All' es",company.rindex('l'))

#17. What character is at index 10 in "Coding For All" string.
print("El carácter en el índice 10 en la cadena 'Coding For All' es",company[10],"un espacio")

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("La abreviatura de 'Python For All' es",chicharito[0] + chicharito[7] + chicharito[11])

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
print("La abreviatura de 'Coding For All' es",company[0] + company[7] + company[11])

#20. Use index to determine the position of the first occurrence of C in Coding For All.
print("El índice en donde esta la posición de la primera aparición de C en 'Coding For All' es",company.index('C'))

#21. Use index to determine the position of the first occurrence of F in Coding For All.
print("El índice en donde esta la posición de la primera aparición de F en 'Coding For All' es",company.index('F'))

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
konan_big = 'Coding For All People'
print("La posición de la última aparición de l en 'Coding For All People' es",konan_big.rfind('l'))

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.
eeaa = 'You cannot end a sentence with because because because is a conjunction'
print("La posición de la primera aparición de 'because' en 'You cannot end a sentence with because because because is a conjunction' es",eeaa.index('because')) #31

#24. Use rindex to find the position of the last occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.
print("La posición de la última aparición de 'because' en 'You cannot end a sentence with because because because is a conjunction' es",eeaa.rindex('because')) #47

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.
print(eeaa[0:30] + eeaa[54:71])

#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.
print("La posición de la primera aparición de 'because' en 'You cannot end a sentence with because because because is a conjunction' es",eeaa.find('because')) #31

#27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.
print(eeaa[0:30] + eeaa[54:71])

#28. Does ''Coding For All' start with a substring Coding?
print("¿'Coding For All' comienza con una subcadena 'Coding'?",company.startswith('Coding'))

#29. Does 'Coding For All' end with a substring coding?
print("¿'Coding For All' termina con una subcadena 'coding'?",company.endswith('coding'))

#30. '   Coding For All      ', remove the left and right trailing spaces in the given string.
company_space = '   Coding For All      '
print(company_space[3:17])

#31. Which one of the following variables return True when we use the method isidentifier(): '30DaysOfPython' o 'thirty_days_of_python'.
changi = '30DaysOfPython'
chuyita = 'thirty_days_of_python'
print("¿Para la variable '30DaysOfPython' devuelve Verdadero cuando usamos el método isidentifier()",changi.isidentifier())
print("¿Para la variable 'thirty_days_of_python' devuelve Verdadero cuando usamos el método isidentifier()",chuyita.isidentifier())

#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
chido = ' '.join(python_libraries)
print(chido)

#33. Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

#34. Use a tab escape sequence to write the following lines.
print("Name\t\tAge\tCountry\t\tCity\nOctavio\t\t18\tMéxico\t\tAguascalientes")

#35. Use the string formatting method to display the following:
radio = 10
area = 3.14 * radio ** 2
print('El área del circulo con radio {} son {} metros cuadrados.'.format(radio,area))