
b = -1
c = 1
while True:

    try:
        a = int(input("\nВведіть будь яке ціле число: "))
    except ValueError:
        print("\n---Введіть ціле число!!!--- ")
        continue
    b += a
    c += a
    print("\nПопереднє ціле число перед", a, ": ", b)
    print("\nНаступне ціле число після", a, ": ", c)
    b = -1
    c = 1
    d = input("Хочете вийти y/n ? ")
    if d == "y":
        exit()
    else:
        pass
