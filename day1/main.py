with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]
    lst1, lst2 = zip(*[line.replace("   ", " ").split(" ") for line in lines])
    lst1, lst2 = sorted(lst1), sorted(lst2)

    # First part
    result = 0
    for val1, val2 in zip(lst1, lst2):
        result += abs(int(val1) - int(val2))
    
    print(result)

    # Second part
    result = 0
    for num in lst1:
        result += int(num) * lst2.count(num)
    print(result)

