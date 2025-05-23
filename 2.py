def divide_hundred(x):
    try:
        result = 100 / float(x)
        return result
    except ValueError:
        return "Ошибка: Вы ввели не число."
    except ZeroDivisionError:
        return "Ошибка: Нельзя делить на ноль."
user_input = input("Введите число, на которое разделить 100: ")

output = divide_hundred(user_input)

print(output)
