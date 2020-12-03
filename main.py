# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def day1_1():
    input = open("day1-input.txt", "r")
    lines = input.readlines()

    numbers = set()
    for line in lines:
        number = int(line)
        if 2020 - number in numbers:
            print(2020 - number, number, (2020-number) * number)
        numbers.add(number)

def day1_2():
    input = open("day1-input.txt", "r")
    lines = input.readlines()

    numbers = set()
    for line in lines:
        number = int(line)
        numbers.add(number)

    numberPairs = set()
    for number1 in numbers:
        for number2 in numbers:
            numberPairs.add((number1, number2))

    for pair in numberPairs:
        if 2020 - (pair[0] + pair[1]) in numbers:
            print(pair[0], pair[1], 2020 - (pair[0] + pair[1]), pair[0] * pair[1] * (2020 - (pair[0] + pair[1])))

def day2_1():
    input = open("day2-input.txt", "r")
    lines = input.readlines()

    valid = 0
    for line in lines:
        values = line.split()
        cnt = values[2].count(values[1][0])
        min = int(values[0].split(sep="-")[0])
        max = int(values[0].split(sep="-")[1])
        if min <= cnt <= max:
            valid += 1
    print(valid)


def day2_2():
    input = open("day2-input.txt", "r")
    lines = input.readlines()

    valid = 0
    for line in lines:
        values = line.split()
        char = values[1][0]
        p1 = int(values[0].split(sep="-")[0]) - 1
        p2 = int(values[0].split(sep="-")[1]) - 1

        string = values[2]
        text = string[p1] + string[p2]
        if text.count(char) == 1:
            valid += 1
    print(valid)


def day3_12():
    input = open("day3-input.txt", "r")
    lines = input.readlines()

    numbers = set()

    t1 = t2 = t3 = t4 = t5 = 0
    x1 = x2 = x3 = x4 = x5 = 0
    y = True

    for line in lines:
        if line[x1 % (len(line)-1)] == "#":
            t1 += 1
        if line[x2 % (len(line) - 1)] == "#":
            t2 += 1
        if line[x3 % (len(line) - 1)] == "#":
            t3 += 1
        if line[x4 % (len(line) - 1)] == "#":
            t4 += 1
        x1 += 1
        x2 += 3
        x3 += 5
        x4 += 7

        if y:
            if line[x5 % (len(line) - 1)] == "#":
                t5 += 1
            x5 += 1
        y = not y

    print(t2)
    print(t1 * t2 * t3 * t4 * t5)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day3_12()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
