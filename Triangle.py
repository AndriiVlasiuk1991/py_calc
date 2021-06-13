from math import *

title = "Розрахунок парамеирів прямокутного трикутника"

def help():
    print("_" * 50)
    print("{!s}{}".format("| Оберіть, який з параметрів потрібно розрахувати?:".ljust(60, ), "|"))
    print("{!s}{}".format("| Для розрахунку площі введіть \"S\": ".ljust(60, ), "|"))
    print("{!s}{}".format("| Для розрахунку периметру введіть \"P\": ".ljust(60, ), "|"))
    print("{!s}{}".format("| Для розрахунку висоти введіть \"H\": ".ljust(60, ), "|"))
    print("{!s}{}".format("| Для розрахунку катета введіть \"A\" або \"B\": ".ljust(60, ), "|"))
    print("{!s}{}".format("| Для розрахунку гіпотенузи введіть \"С\" : ".ljust(60, ), "|"))
    print("_" * 50)

def triangle():
    print("\t\t\t|\ ")
    print("\t\t\t|", "\ ")
    for i in range(0, 20):
        if i == 10:
            print("\t\t\t|B", " "*(i-1), "\C ")
        else:
            print("\t\t\t|", " " * i, "\ ")
        i += 1
    print("\t\t\t|", "_" * 20, "\ ")
    print("\t\t\t", " " * 10, "A")


def data():
    a = int(input("Введіть довжину катета А: "))
    b = int(input("Введіть довжину катета В: "))
    c = input("Введіть довжину гіпотенузи С: ")
    h = input("Введіть висоту H: ")
    ac = input("Введіть значення кута AC: ")
    bc = input("Введіть значення кута BC: ")
    return (a, b, c, h, ac, bc)

def area():
    a = int(input("Введіть довжину катета в сантиметрах А: "))
    b = int(input("Введіть довжину катета в сантиметрах В: "))
    s = (a + b) / 2
    print("Площа прямокутного трикутника S = ", int(s), "(см2)")
    return s

def per():
    a = int(input("Введіть довжину катета в сантиметрах А: "))
    b = int(input("Введіть довжину катета в сантиметрах В: "))
    c = int(input("Введіть довжину гіпотенузи С: "))
    p = a + b + c
    print("Периметр прямокутного трикутника Р = ", int(p), "(см)")
    return p

def height():
    a = int(input("Введіть довжину катета в сантиметрах А: "))
    b = int(input("Введіть довжину катета в сантиметрах В: "))
    c = int(input("Введіть довжину гіпотенузи С: "))
    h = (a * b) / c
    print("Высота прямокутного трикутника S = ", int(h), "(см)")
    return h

def legA():
    b = int(input("Введіть довжину катета в сантиметрах В: "))
    c = int(input("Введіть довжину гіпотенузи С: "))
    a = sqrt(pow(c, 2) - pow(b, 2))
#    a = c * sin(bc)
#    a = b * cos(ac)
#    a = b * tan(bc)
    print("Катет А = ", round(float(a), 2), "(см)")
    return a

def legB():
    a = int(input("Введіть довжину катета в сантиметрах А: "))
    c = int(input("Введіть довжину гіпотенузи С: "))
    b = sqrt(pow(c, 2) - pow(a, 2))
#    b = c * sin(ac)
#    b = a * cos(bc)
#    b = a * tan(ac)
    print("Катет А = ", round(float(b), 2), "(см)")
    return b

def hyp():
    a = int(input("Введіть довжину катета в сантиметрах А: "))
    b = int(input("Введіть довжину катета в сантиметрах В: "))
    c = sqrt(pow(a, 2) + pow(b, 2))
#   c = a / sin(ac)
#   c = b / sin(bc)
#   a = a / cos(bc)
#   a = b / cos(ac)
    print("Катет А = ", round(float(c), 2), "(см)")
    return c

def main():
    triangle()
    help()
    v = input("Хочу розрахувати: ")

    if (v == "S" or v == "s"):
        area()
    elif (v == "P" or v == "p"):
        per()
    elif (v == "H" or v == "h"):
        height()
    elif (v == "H" or v == "h"):
        height()
    elif (v == "A" or v == "a" or v == "B" or v == "b"):
        if (v == "A" or v == "a"):
            legA()
        elif (v == "B" or v == "b"):
            legB()
    elif (v == "C" or v == "c"):
        hyp()

if __name__=="__main__":
    main()