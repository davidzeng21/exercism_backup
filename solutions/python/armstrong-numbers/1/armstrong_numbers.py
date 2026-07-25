def is_armstrong_number(number):
    pass
    number_of_digits = 0
    temp = number
    while temp // 10 ** number_of_digits != 0:
        number_of_digits += 1
    total = 0
    remaining = number
    while remaining > 0:
        digit = remaining % 10
        total += digit ** number_of_digits
        remaining //= 10
    return number == total
