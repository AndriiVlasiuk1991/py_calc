#title here

title = "Calculator"
print("\nWelcome to ", title, "\n")
print("Інструкція:\n\t+ - додати\n\t- - відняти\n\t* - помножити\n\t/ - поділити\n\t// - поділити по модулю\n\t** - степінь числа\n\t% - залишок від ділення\n\texit - вийти з", title, "\n")



while True:
    a = int(input("Введіть перше значення: "))
    c = input("Введіть арифметичний оператор: ")
    b = int(input("Введіть друге значення: "))

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

    d = input(exit)