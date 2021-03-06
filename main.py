import re


def day1_1():
    input = open("day1-input.txt", "r")
    lines = input.readlines()

    numbers = set()
    for line in lines:
        number = int(line)
        if 2020 - number in numbers:
            print(2020 - number, number, (2020 - number) * number)
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
        if line[x1 % (len(line) - 1)] == "#":
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


def day4_1():
    input = open("day4-input.txt", "r")
    lines = input.readlines()

    d = {}
    valid = 0
    for line in lines:
        line = line.rstrip('\n')
        if line == "":
            if set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]).issubset(set(d.keys())):
                valid += 1
            d = {}
            continue

        pairs = line.split()
        for pair in pairs:
            key, value = pair.split(":")
            d[key] = value
    print(valid)


def day4_2():
    input = open("day4-input.txt", "r")
    lines = input.readlines()

    d = {}
    valid = 0
    for line in lines:
        line = line.rstrip('\n')
        if line == "":
            if not {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(set(d.keys())):
                d = {}
                continue

            if not 1920 <= int(d["byr"]) <= 2002:
                d = {}
                continue

            if not 2010 <= int(d["iyr"]) <= 2020:
                d = {}
                continue

            if not 2020 <= int(d["eyr"]) <= 2030:
                d = {}
                continue

            if not (len(d["hcl"]) == 7 and d["hcl"][0] == "#"):
                d = {}
                continue

            try:
                int(d["hcl"][1:8], 16)
            except:
                print("found bad color")
                d = {}
                continue

            if not ((d["hgt"].endswith("cm") and len(d["hgt"]) == 5 and 150 <= int(d["hgt"][0:3]) <= 193) or
                    (d["hgt"].endswith("in") and len(d["hgt"]) == 4 and 59 <= int(d["hgt"][0:2]) <= 76)):
                d = {}
                continue

            if d["ecl"][0:3] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                d = {}
                continue

            if not len(d["pid"]) == 9:
                d = {}
                continue

            try:
                int(d["pid"])
            except:
                d = {}
                continue

            valid += 1
            d = {}

        pairs = line.split()
        for pair in pairs:
            key, value = pair.split(":")
            d[key] = value
    print(valid)

def day5_1():
    input = open("day5-input.txt", "r")
    lines = input.readlines()

    max_id = 0
    for line in lines:
        row_code = line[0:7]
        col_code = line[7:10]

        row_bytes = row_code.replace("F", "0").replace("B", "1")
        row_num = int(row_bytes, base=2)

        col_bytes = col_code.replace("L", "0").replace("R", "1")
        col_num = int(col_bytes, base=2)

        seat_id = row_num * 8 + col_num
        max_id = max(max_id, seat_id)

    print(max_id)


def day5_2():
    input = open("day5-input.txt", "r")
    lines = input.readlines()

    s = set()
    p = set()
    for line in lines:
        row_code = line[0:7]
        col_code = line[7:10]

        row_bytes = row_code.replace("F", "0").replace("B", "1")
        row_num = int(row_bytes, base=2)

        col_bytes = col_code.replace("L", "0").replace("R", "1")
        col_num = int(col_bytes, base=2)

        seat_id = row_num * 8 + col_num
        s.add(seat_id)

        if seat_id in p:
            p.remove(seat_id)
        if seat_id + 1 not in s and seat_id + 2 in s:
            p.add(seat_id + 1)
        if seat_id - 1 not in s and seat_id - 2 in s:
            p.add(seat_id - 1)

    print(p)


def day6_1():
    input = open("day6-input.txt", "r")
    lines = input.readlines()

    suma = 0
    s = set()
    for line in lines:
        line = line.rstrip('\n')
        if line == "":
            suma += len(s)
            s = set()

        for letter in line:
            s.add(letter)

    print(suma)


def day6_2():
    input = open("day6-input.txt", "r")
    lines = input.readlines()

    suma = 0
    s = set()
    first = True
    for line in lines:
        line = line.rstrip('\n')
        if line == "":
            suma += len(s)
            s = set()
            first = True
            continue

        user_set = set()
        for letter in line:
            user_set.add(letter)

        if first:
            first = False
            s = user_set
            continue
        else:
            s = s.intersection(user_set)

    print(suma)


def day7_1():
    input = open("day7-input.txt", "r")
    lines = input.readlines()

    bagjacency_list = {}
    for line in lines:
        line = line.rstrip('\n')
        key, contents = line.split(sep=" bags contain ")
        for sub in ["no other bags", " bags", " bag", "."]:
            contents = contents.replace(sub, "")
        contents = contents.split(sep=", ")

        for bag_type in contents:
            bag_split = bag_type.split()
            if len(bag_split) == 0:
                continue
            count = int(bag_split[0])
            type = " ".join(bag_split[1:])

            if type not in bagjacency_list:
                bagjacency_list[type] = set()
            if key not in bagjacency_list:
                bagjacency_list[key] = set()
            bagjacency_list[type].add(key)

    visited = set()
    to_visit = ["shiny gold"]
    while len(to_visit) > 0:
        current = to_visit.pop()
        visited.add(current)
        for neighbor in bagjacency_list[current]:
            if neighbor not in visited:
                to_visit.append(neighbor)

    print(len(visited)-1)



def day7_2():
    input = open("day7-input.txt", "r")
    lines = input.readlines()

    bagjacency_list = {}
    for line in lines:
        line = line.rstrip('\n')
        key, contents = line.split(sep=" bags contain ")
        for sub in ["no other bags", " bags", " bag", "."]:
            contents = contents.replace(sub, "")
        contents = contents.split(sep=", ")

        if key not in bagjacency_list:
            bagjacency_list[key] = set()

        for bag_type in contents:
            bag_split = bag_type.split()
            if len(bag_split) == 0:
                continue
            count = int(bag_split[0])
            type = " ".join(bag_split[1:])

            if type not in bagjacency_list:
                bagjacency_list[type] = set()
            bagjacency_list[key].add((type, count))

    def visit(to_visit, count):
        if len(bagjacency_list[to_visit]) == 0:
            return count
        sum = 0
        for neighbor, i in bagjacency_list[to_visit]:
            sum += visit(neighbor, i)
        return sum * count + count

    print(visit("shiny gold", 1) - 1)


if __name__ == '__main__':
    day7_2()
