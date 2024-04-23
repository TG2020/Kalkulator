import logging


def calc(wybor, num1, num2):
    dict = {
        "+": lambda: num1 + num2,
        "-": lambda: num1 - num2,
        "*": lambda: num1 * num2,
        "/": lambda: num1 / num2,
        "**": lambda: num1 ** num2,
        }.get(wybor, lambda : None)()
    return dict

print("Wybierz operację: +. Dodawanie ,-. Odejmowanie ,*. Mnożenie ,/. Dzielenie ,**. Potęgowanie ")
wybor = input()
num1 = float(input("Podaj pierwszy składnik: "))
num2 = float(input("Podaj drugi składnik: "))

if __name__ == "__main__":
    print(f"Wynik: {num1} {wybor} {num2} =", calc(wybor, num1, num2),)
