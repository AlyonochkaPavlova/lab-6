def divisible_by_three(number):
    if number % 3 == 0:
        return True
    else:
        return False
num = int(input("Введите число: "))

if divisible_by_three(num):
    print("Да, число делится на 3.")
else:
    print("Нет, число не делится на 3.")
