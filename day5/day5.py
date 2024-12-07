from collections import defaultdict

def part1(file_line):
    rules = defaultdict(list)
    stophere = 0

    for i in range(len(file_line)):
        line = file_line[i].strip()
        if not line:
            continue
        if '|' in line:
            num1, num2 = line.split('|')
            rules[int(num1)].append(int(num2))
        else:
            stophere = i
            break

    updates = []
    for i in range(stophere, len(file_line)):
        line = file_line[i].strip()
        if not line:
            continue
        updates.append(list(map(int, line.split(','))))

    correct_updates = []
    for update in updates:
        if is_update_correct(update, rules):
            correct_updates.append(update)

    res = 0
    for update in correct_updates:
        mid = update[len(update) // 2]
        res += mid

    return res

def is_update_correct(update, rules):
    """Check if an update is in the correct order based on the rules."""
    for key in rules:
        if key in update:
            for value in rules[key]:
                if value in update:
                    if update.index(key) > update.index(value):
                        return False
    return True

def part2(file_line):
    pass

def main():
    with open("day5/input.in", "r") as inFile:
        file_line = inFile.readlines()
        result = part1(file_line)
        print(result)

if __name__ == "__main__":
    main()
