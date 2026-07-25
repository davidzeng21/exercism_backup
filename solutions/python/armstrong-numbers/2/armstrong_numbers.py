def is_armstrong_number(number):
    digits = str(number)
    num_digits = len(digits)
    total = sum(int(d) ** num_digits for d in digits)
    return number == total
