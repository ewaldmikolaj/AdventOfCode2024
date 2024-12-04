import re

with open("input.txt", "r") as file:
    memory = file.read()

    result = 0
    enabled = True
    operations = re.finditer(r"(mul\(\d{1,3}\,\d{1,3}\)|(don't\(\))|(do\(\)))", memory)
    for op in operations:
        if op.group() == "don't()":
            enabled = False
        elif op.group() == "do()":
            enabled = True
        else:
            if enabled:
                numbers = re.findall(r"\d{1,3}", op.group())
                first, second = numbers
                result += int(first) * int(second)

    print(result)
        