import logging


def calc(wybor, num1, num2):
    dict = {
        "1": lambda: num1 + num2,
        "2": lambda: num1 - num2,
        "3": lambda: num1 * num2,
        "4": lambda: num1 / num2,
        "5": lambda: num1 ** num2,
        }.get(wybor, lambda : None)()
    return dict

print("Wybierz operację: 1. Dodawanie ,2. Odejmowanie ,3. Mnożenie ,4. Dzielenie ,5. Potęgowanie ")
wybor = input()
num1 = float(input("Podaj pierwszy składnik: "))
num2 = float(input("Podaj drugi składnik: "))

if __name__ == "__main__":
    print("Wynik działania to: ", calc(wybor, num1, num2))
