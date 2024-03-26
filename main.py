def main():
    try:
        input_string = input("Введіть список чисел, відокремлених комами: ")

        numbers = [int(num.strip()) for num in input_string.split(",")]

        print("Список чисел:", numbers)

    except ValueError:
        print("Помилка: Введені дані не можуть бути перетворені у цілі числа.")
    except IndexError:
        print("Помилка: Доступ за межі діапазону списку.")

if __name__ == "__main__":
    main()
