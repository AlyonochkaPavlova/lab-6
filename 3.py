def is_magic_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    last_two_digits = year % 100
    return day * month == last_two_digits
user_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if is_magic_date(user_date):
    print("Магическая дата!")
else:
    print("Не магическая дата.")
