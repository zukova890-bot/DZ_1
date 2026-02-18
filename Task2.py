x = input("Введите число: ")

try:
    if int(x)<=0:
        print("Ошибка: введено не положительное число")
    else:
        if int(x)%2 == 0:
            print(f"Число {x} является чётным")
        else:
            print(f"Число {x} не является чётным")
except ValueError:
    print("Ошибка: введено не число")