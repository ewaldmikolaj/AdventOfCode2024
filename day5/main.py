import re
from collections import defaultdict


def check_correctness(index: int, update: list, rules: dict) -> bool:
    number = update[index]
    for page in update[index + 1:]:
        if not rules.get(number) or page not in rules.get(number):
            return False
    return True

def fix_invalid(index: int, update: list, rules: dict) -> None:
    number = update[index]
    for key, values in rules.items():
        if number in values and key in update[index + 1: ]:
            a, b = update.index(number), update.index(key)
            update[b], update[a] = update[a], update[b]
            break


with open("input.txt", "r") as file:
    rules, updates = defaultdict(list), []
    for line in file:
        content = line.strip()
        if re.match(r"\d+\|\d+", content):
            key, value = (content.split("|"))
            rules[key].append(value)
        elif content == "":
            ...
        else:
            updates.append(content.split(","))

    # part one
    result1, result2 = 0, 0
    invalid = []
    for update in updates:
        for it in range(len(update) - 1):
            if not check_correctness(it, update, dict(rules)):
                invalid.append(update)
                break
        else:
            result1 += int(update[len(update) // 2])

    for update in invalid:
        for it in range(len(update) - 1):
            while not check_correctness(it, update, dict(rules)):
                fix_invalid(it, update, rules)
        else:
            result2 += int(update[len(update) // 2])
            print(result2)

    print("part one: ", result1)
    print("part two: ", result2)
        
    