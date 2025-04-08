#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
def list_of_hexa_colors (n):
    hex_colors = ['#' + ''.join(random.choices('0123456789abcdef',k=6)) for _ in range(n)]
    return hex_colors
print(list_of_hexa_colors(5))

#2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors (n):
    rgb_colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(n)]
    return rgb_colors
print(list_of_rgb_colors(5))

#3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors (item,n):
    for _ in range(n):
        if item == 'hexa':
            color = ['#' + ''.join(random.choices('0123456789abcdef',k=6)) for _ in range(n)]
        else:
            item == 'rgb'
            color = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(n)]
    return color
print(generate_colors('rgb',5))

print("Revisado")