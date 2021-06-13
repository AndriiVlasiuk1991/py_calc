from math import *

#title here

title = "Calculator"

def Hello():
    print("\n---Welcome to ", title, "---\n")

def help():
    print("_" * 50)
    print("{!s}{}".format("| Інструкція:".title().ljust(51, ), "|"))
    print("{!s}{}".format("| \t   + - додати".title().ljust(50, ), "|"))
    print("{!s}{}".format("| \t   - - відняти".title().ljust(50, ), "|"))
    print("{!s}{}".format("| \t   * - помножити".title().ljust(50, ), "|"))
    print("{!s}{}".format("| \t   / - поділити".title().ljust(50, ), "|"))
    print("{!s}{}".format("| \t   // - поділити".title().ljust(50, ), "|"))
    print("{!s}{}".format("| \t   ** - степінь числа".title().ljust(50, ), "|"))
    print("{!s}{}".format("| \t   % - залишок від ділення".title().ljust(50, ), "|"))
    print("_" * 50)
#   return input()

def Exit():
    d = input("Продовжити? Enter / n: ")
    return d

def oper(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "**":
        return x ** z
    elif y == "/":
        return x / z
    elif y == "//":
        return x // z
    elif y == "%":
        return x % z
    elif y == "sin":
       return sin(z)
    elif y == "cos":
       return cos(z)
    elif y == "tan":
       return tan(z)

def formula():
    return input("Введіть формулу у форматі \"a + b\": ")



def main():
    Hello()
    help()
    while True:

        try:
            x, y, z = formula().split(" ")
            try:
                x = int(x)
                z = int(z)
            except ValueError:
                print("---Ви ввели не число!!!--- \n ---Введіть ціле число!!!---")
                continue
        except ValueError:
            print("---Ви ввели невірний формат формули!!!---")
            continue

        if (y == "+" or y == "-" or y == "*" or y == "**"):
            res = oper(x, y, z)
            print(f"{x} {y} {z} = {res}")
        elif (y == "/" or y == "//" or y == "%"):
            if z != 0:
                res = oper(x, y, z)
                print(f"{x} {y} {z} = {res}")
            else: print("Не можна ділити на \"0\" \n")
        elif y == "sin":
            res = oper(x, y, z)
            print(f"{y} {z} = {res}")
        else:
            print("---Ви ввели невірний арифметичний оператор!!!---\n")
            continue


        if Exit() == "n":
            print("\n---Кінець---")
            break
        else:
            pass

if __name__=="__main__":
    main()

