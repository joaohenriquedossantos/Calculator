import os
from calculator_arts import logo_art, calculator_art

def add(first_value: float, second_value: float):
    return first_value + second_value


def subtract(first_value: float, second_value: float):
    return first_value - second_value


def multiply(first_value: float, second_value: float):
    return first_value * second_value


def divide(first_value: float, second_value: float):
    try:
        return first_value / second_value
    except ZeroDivisionError:
        return ZeroDivisionError

clear_console = lambda: os.system("clear")

operations = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide,
}

option = 0
clear_console()

logo_art()
calculator_art()

def main():
    option = int(input("\n [1] Add \n [2] Subtract \n [3] Multiply \n [4] Divide \n [5] Clear Console \n \n Select an option: "))
    if option == 5:
        clear_console()
        main()

    first_value = float(input("\nType the first value: "))
    second_value = float(input("Type the second value: "))
    execute_operation = operations[option]

    print(f"\nYour result: {execute_operation(first_value, second_value)}")

    ask_to_exit = int(input("\n [0] No \n [1] Yes \n \n Would you like to exit? "))

    if ask_to_exit != 1:
        main()

main()