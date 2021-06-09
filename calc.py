#title here

title = "Calculator"
print("\nWelcome to ", title, "\n")
print("Інструкція:\n\t+ - додати\n\t- - відняти\n\t* - помножити\n\t/ - поділити\n\t// - поділити по модулю\n\t** - степінь числа\n\t% - залишок від ділення", title, "\n")


while True:
    try:
        a = int(input("Введіть перше значення: "))
    except ValueError:
        print("Введіть ціле число: \n")
        continue

    c = input("Введіть арифметичний оператор: ")

    try:
        b = int(input("Введіть друге значення: "))
    except ValueError:
        print("Введіть ціле число: \n")
        continue

    if c == "+":
        print("Результат", a + b, "\n")
    elif c == "-":
        print("Результат", a - b, "\n")
    elif c == "*":
        print("Результат", a * b, "\n")
    elif c == "/":
        if b != 0:
            print("Результат", a / b, "\n")
        else:
            print("Не можна ділити на \"0\" \n")
    elif c == "//":
        print("Результат", a // b, "\n")
    elif c == "**":
        print("Результат", a ** b, "\n")
    elif c == "%":
        print("Результат", a % b, "\n")
    else:
        print("---Ви ввели невірний арифметичний оператор!!!---\n")
        continue

    d = input("Хочете вийти y/y ? \n")
    if d == "y":
        exit()
    else:
        pass

