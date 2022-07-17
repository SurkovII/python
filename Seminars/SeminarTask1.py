

# num = int(input('Введите число: '))


def progr(num):

    if (num % 10 == 0 or num % 10 == 5 or num % 10 == 6 or num % 10 == 7 or num % 10 == 8 or num % 10 == 9) or ((num//10) % 10 == 1):
        print(f"{num} програмистов")
    elif (num % 10 == 2 or num % 10 == 3 or num % 10 == 4):
        print(f"{num} програмиста")
    elif num % 10 == 1:
        print(f"{num} програмист")


# progr(num)

for i in range(0, 50, 1):
    progr(i)
