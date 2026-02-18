age = input("Введите ваш возраст: ")

try:
    if int(age) < 0:
        print("Ошибка: возраст не может быть отрицательным!")
    else:
        if int(age) >= 18:
            print("Вы совершеннолетний.")
        else:
            print("Вы несовершеннолетний.")
except ValueError:
    print("Ошибка: введено не число!")