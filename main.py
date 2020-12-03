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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day2_2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
