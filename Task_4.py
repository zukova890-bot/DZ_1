while True:
    length = input("Введите число: ")
    if length == "exit":
        print("Выход из программы...")
        break
    if length.isdigit():
        print(f"В этом числе {len(length)} цифры.")
    elif length.lstrip('-').isdigit():
        print(f"В этом числе {len(length)-1} цифры.")
    else:
        print("Ошибка: данные не являются числом")
