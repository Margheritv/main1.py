def circle_area(r1, r2, r3):

    a = pi*(r1**2+r2**2+r3**2)

    return a


r1 = float(2)
r2 = float(3)
r3 = float(4)
pi = 3.14

print("The combined area is: ", circle_area(r1, r2, r3))