import random
import math


# Take user input
def ask_user_info():
    age = input('What is your age?\n')
    name = input('What is your name?\n')
    print('Hello. nice to meet you ' + name)


def calculate():
    principal = float(input('What is your initial capital?'))
    interest = float(input('What is the interest rate?'))
    years = int(input('How long are you planning to invest?'))
    for i in range(years):
        total = principal * float((1 + interest) ** float(i + 1))
        print(f"{i + 1} year and the total is {total:.2f}")


# Similar to do while loop
def test():
    while True:
        try:
            num = int(input("Please enter a number: "))
            break
        except ValueError:
            print('Enter a number you dumb fuck, not a letter ')

    print(num)


# For loop variations
def print_shit():
    for i in range(1, 22):
        if i % 2 != 0:
            print(i)


# Flow controls
def guess_number():
    secret_number = 7
    while True:
        guess = int(input('Please enter a number: '))
        if guess == secret_number:
            print('You guessed it')
            break
        else:
            print('Please try again!')


# String functions
def string_functions(string):
    new = []
    for c in string:
        r = random.randint(0, 1)
        if r == 0:
            new.append(c.upper())
        else:
            new.append(c.lower())
    return ''.join(new)


def hide_string():
    message = str(input("Please enter a string in uppercase: "))
    secret_message = ""
    for c in message:
        secret_message += str(ord(c) - 23)  # works with both lower and uppercase

    norm_string = ""
    for c in range(0, len(secret_message) - 1, 2):
        char_code = secret_message[c] + secret_message[c + 1]
        norm_string += chr(int(char_code) + 23)  # works with both lower and uppercase

    print(f"the secret message converted to Unicode {secret_message}")
    print(f"original message is {norm_string}")


# hide_string()


# Logical thinking, messing with Uni-codes
def caesar_cypher():
    message = input("Please enter a message: ")
    unit_shift = int(input("Please enter the key to be shifted from 1 to 26 (a - z): "))
    encrypted_message = __cipher_helper(message, unit_shift)

    print(f"The encrypted message is: {__cipher_helper(message, unit_shift)}")
    print(f"The decrypted message is: {__cipher_helper(encrypted_message, -unit_shift)}")


def __cipher_helper(message, unit_shift) -> str:
    new_message = ""
    for char in message:
        # Convert the character at i index message into Unicode and add unit shift to it
        char_encode = ord(char)
        char_encode += unit_shift
        # If the character at said index is an alphabetical letter then do these
        if char.isalpha():
            if char.isupper():
                if char_encode > ord("Z"):
                    char_encode -= 26
                elif char_encode < ord("A"):
                    char_encode += 26
            else:
                if char_encode > ord("z"):
                    char_encode -= 26
                elif char_encode < ord("a"):
                    char_encode += 26
            new_message += chr(char_encode)
        else:
            new_message += char

    return new_message


# caesar_cypher()


def __get_prime(num) -> list:
    new = []
    for i in range(1, num, 2):
        if __is_prime(i):
            new.append(i)
    return new


def __is_prime(num) -> bool:
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


def test_prime():
    num = int(input("Please enter number: "))
    list_of_prime = __get_prime(num)
    for i in list_of_prime:
        print(i)


def find_smallest(list_num) -> int:
    smallest_so_far = None
    for i in list_num:
        if i < smallest_so_far:
            smallest_so_far = i
    return smallest_so_far


def find_largest(list_num) -> int:
    largest_so_far = -1
    for i in list_num:
        if i > largest_so_far:
            largest_so_far = i
    return largest_so_far


def get_shape():
    shape = input("Enter the shape: ").lower()
    if shape == "rectangle":
        __rectangle_area()
    elif shape == "circle":
        __circle_area()
    elif shape == "parallelogram":
        __parallelogram_area()
    elif shape == "trapezoid":
        __trapezoid_area()


def __trapezoid_area():
    a_base = float(input("Enter the base of a: "))
    b_base = float(input("Enter the base of b: "))
    height = float(input("Enter the height of the trapezoid: "))
    area = ((a_base + b_base) / 2) * height

    print(f"The area of the trapezoid is {area:.2f}")


def __rectangle_area():
    height = float(input("Enter the height of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = height * width

    print(f"The area of the rectangle is: {area:.2f}")


def __circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * math.pow(radius, 2)

    print(f"The area of the circle is: {area:.2f}")


def __parallelogram_area():
    base = float(input("Enter the base of the parallelogram: "))
    height = float(input("Enter the height of the parallelogram: "))
    area = base * height

    print(f"The area of the parallelogram is: {area:.2f}")


def random_list():
    new = []
    for i in range(5):
        new.append(random.randrange(1, 9))

    for i in new:
        print(i)


def count_dice():
    num_rolled = int(input("Enter the number of dice that will be rolled: "))
    new = []
    for i in range(num_rolled):
        new.append(random.randint(1, 6))
    __count_occurrence(new)


def __count_occurrence(arr):
    dice1, dice2, dice3, dice4, dice5, dice6 = 0, 0, 0, 0, 0, 0
    for i in arr:
        if i == 1:
            dice1 += 1
        elif i == 2:
            dice2 += 1
        elif i == 3:
            dice3 += 1
        elif i == 4:
            dice4 += 1
        elif i == 5:
            dice5 += 1
        else:
            dice6 += 1
    result = f"Dice 1: {dice1}\nDice 2: {dice2}\nDice 3: {dice3}\nDice 4: {dice4}\nDice 5: {dice5}\nDice 6: {dice6}"
    print(result)


def bubble_sort(list_arr):
    for i in range(len(list_arr)):
        for j in range(0, len(list_arr) - i - 1):
            if list_arr[j] > list_arr[j + 1]:
                list_arr[j], list_arr[j + 1] = list_arr[j + 1], list_arr[j]

    for i in list_arr:
        print(i, end=" ")


def main():
    # test_prime()
    # print(find_largest([1, 2, 6, 4]))
    # get_shape()
    random_list()
    bubble_sort([4, 5, 2, 3, 1])
    count_dice()


if __name__ == "__main__":
    main()