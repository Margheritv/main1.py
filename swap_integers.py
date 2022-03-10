def swap_integers(num1, num2):
    print("X=", num1)
    print("Y=", num2)
    print("")

    z = num1
    num1 = num2
    num2 = z
    print("After swap:")
    print("X=", num1)
    print("Y=", num2)

    return_value = str(num1) + str(num2)
    return return_value


x = 10
y = 22

print("Return value: ", swap_integers(x, y))