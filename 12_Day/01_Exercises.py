#1. Writ a function which generates a six digit/character random_user_id.
import random
import string
def random_user_id ():
    return ''.join(random.choices(string.ascii_letters + string.digits,k=6))
print("Tu ID es:",random_user_id())


#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user ():
    num_caracters = int(input("¿Cuantos caracteres? "))
    num_IDS = int(input("¿Cuantos IDs quiere generar? "))
    for _ in range(num_IDS):
        IDs = ''.join(random.choices(string.ascii_letters + string.digits,k=num_caracters))
        print(IDs)
user_id_gen_by_user()

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
import random
def rgb_color_gen ():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return f"RGB({red},{green},{blue})"
print(rgb_color_gen())