def is_lucky_ticket(ticket_number):
    length = len(ticket_number)
    half_length = length // 2

    first_half_sum = sum(map(int, ticket_number[:half_length]))
    second_half_sum = sum(map(int, ticket_number[half_length:]))
    return first_half_sum == second_half_sum
ticket_num = input("Введите номер билета: ")
if is_lucky_ticket(ticket_num):
    print("Ваш билет счастливый!")
else:
    print("К сожалению, ваш билет несчастливый.")
