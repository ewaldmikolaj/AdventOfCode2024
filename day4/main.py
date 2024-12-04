def check_forwards(x: int, y: int, data: list) -> int:
    return 1 if "".join(data[x][y : y + 4]) == "XMAS" else 0

def check_backwards(x: int, y: int, data: list) -> int:
    if y - 3 < 0:
        return 0
    return 1 if "".join(data[x][y - 3 : y + 1][::-1]) == "XMAS" else 0

def check_vertical_up(x: int, y: int, data: list) -> int:
    if x - 3 < 0:
        return 0
    result = "".join([data[x - it][y] for it in range(4)])
    return 1 if result == "XMAS" else 0

def check_vertical_down(x: int, y: int, data: list) -> int:
    if x + 3 >= len(data):
        return 0
    result = "".join([data[x + it][y] for it in range(4)])
    return 1 if result == "XMAS" else 0

def check_diagonal_up_left(x: int, y: int, data: list) -> int:
    if x - 3 < 0 or y - 3 < 0:
        return 0
    result = "".join([data[x - it][y - it] for it in range(4)])
    return 1 if result == "XMAS" else 0

def check_diagonal_up_right(x: int, y: int, data: list) -> int:
    if x - 3 < 0 or y + 3 >= len(data[x]):
        return 0
    result = "".join([data[x - it][y + it] for it in range(4)])
    return 1 if result == "XMAS" else 0

def check_diagonal_down_left(x: int, y: int, data: list) -> int:
    if x + 3 >= len(data) or y - 3 < 0:
        return 0
    result = "".join([data[x + it][y - it] for it in range(4)])
    return 1 if result == "XMAS" else 0

def check_diagonal_down_right(x: int, y: int, data: list) -> int:
    if x + 3 >= len(data) or y + 3 >= len(data[x]):
        return 0
    result = "".join([data[x + it][y + it] for it in range(4)])
    return 1 if result == "XMAS" else 0

def part_one():
    with open("input.txt", "r") as file:
        data = [list(line.rstrip()) for line in file]

        result = 0
        for x_it in range(len(data)):
            for y_it in range(len(data[x_it])):
                if data[x_it][y_it] == "X":
                    result += check_forwards(x_it, y_it, data)
                    result += check_backwards(x_it, y_it, data)
                    result += check_vertical_up(x_it, y_it, data)
                    result += check_vertical_down(x_it, y_it, data)
                    result += check_diagonal_up_left(x_it, y_it, data)
                    result += check_diagonal_up_right(x_it, y_it, data)
                    result += check_diagonal_down_left(x_it, y_it, data)
                    result += check_diagonal_down_right(x_it, y_it, data)

        print(result)


def check_left(x: int, y: int, data: list) -> bool:
    if data[x - 1][y - 1] == "M" and data[x + 1][y + 1] == "S":
        return True
    if data[x - 1][y - 1] == "S" and data[x + 1][y + 1] == "M":
        return True
    return False

def check_right(x: int, y: int, data: list) -> bool:
    if data[x - 1][y + 1] == "M" and data[x + 1][y - 1] == "S":
        return True
    if data[x - 1][y + 1] == "S" and data[x + 1][y - 1] == "M":
        return True
    return False

def part_two():
    with open("input.txt", "r") as file:
        data = [list(line.rstrip()) for line in file]

        result = 0
        for x_it in range(1, len(data) - 1):
            for y_it in range(1, len(data[x_it]) - 1):
                if data[x_it][y_it] == "A":
                    if check_left(x_it, y_it, data) and check_right(x_it, y_it, data):
                        result += 1

        print(result)

part_one()
part_two()