def triangle(rows):
    for i in range(1, rows + 1):

        for star in range(1, i + 1):
            print("*", end="")  # parameter, makes sure no line is added, just a whitespace
        for space in range(1, (rows - i) + 1):
            print(" ", end="")
        print()  # leere parentesi = spazio vuoto


h = int(4)  # TOTROWS = Height
triangle(h)