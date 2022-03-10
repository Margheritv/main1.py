r1 = float(input('Insert first radius: '))
p = 3.14
a1 = p*r1*r1
print(a1)

r2 = float(input("Insert second radius: "))
a2 = p*r2*r2
print(a2)

r3 = float(input("Insert third radius: "))
a3 = p*r3*r3
print(a3)


def num_concat(a1, a2, a3):

    a1 += a2
    a2 += a3
    a3 += a1

    return int(a1), int(a2), int(a3)

print("The area as a combined integer is: ", int(a1),int(a2),int(a3))

