def check_numbers(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
        return True
    else:
        return False


x = 6
z = 10

print(check_numbers(int(x), int(z)))