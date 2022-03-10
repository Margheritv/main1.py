def sum_up(num1, num2):
    if num2 < num1:
        return 0
    elif num1 and num2 < 0:
        return 0
    else:
        x = num2 - num1
        SumTemp = num1
        Add = num1 + 1
        for i in range(x):
            SumTemp = SumTemp + Add
            Add = Add + 1

    return SumTemp


n = 3
y = 9

print(sum_up(int(n), int(y)))









