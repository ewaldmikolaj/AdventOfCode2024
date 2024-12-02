import itertools

def problem_dampener(report: list) -> bool:
    for it in range(len(report)):
        copy = report.copy()
        del copy[it]
        if first_check(copy) and second_check(copy):
            return True
        
    return False

def first_check(report: list) -> bool:
    for v1, v2 in itertools.pairwise(report):
        diff = abs(int(v1) - int(v2))
        if diff < 1 or diff > 3:
            return False
        
    return True

def second_check(report: list) -> bool:
    order = 0
    for v1, v2 in itertools.pairwise(report):
        order += 1 if int(v1) > int(v2) else 0
    
    return True if order == 0 or order == len(report) - 1 else False

with open("input.txt", "r") as file:
    lines = [line.rstrip().split(" ") for line in file]
    
    result = 0
    for report in lines:
        if first_check(report) and second_check(report):
            result += 1
        elif problem_dampener(report):
            result += 1

    print(result)