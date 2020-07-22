number = input()
num2 = number

while True:
    length = len(number)
    if length % 2 == 0:
        p1 = number[:length // 2]
        p2 = p1 + p1[::-1]
        if int(p2) > int(num2):
            print(p2)
            break
        number = str(int(p1) + 1) + number[length // 2:]
    else:
        p1 = number[:length // 2]
        p2 = p1 + number[length // 2] + p1[::-1]
        if int(p2) > int(num2):
            print(p2)
            break
        number = str(int(p1 + number[length // 2]) + 1) + number[length // 2 + 1:]
