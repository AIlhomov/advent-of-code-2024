inFile = open("day2/input.in", "r")

def countAdjDiff(lst):
    for i in range(len(lst)-1):
        if abs(lst[i+1] - lst[i]) > 3:
            return False
    return True

def is_increasing(lst):
    return all(lst[i] < lst[i+1] for i in range(len(lst)-1)) and countAdjDiff(lst)

def is_decreasing(lst):
    return all(lst[i] > lst[i+1] for i in range(len(lst)-1)) and countAdjDiff(lst)

def part1(reports):
    return is_increasing(reports) or is_decreasing(reports)

def part2(reports):
    if part1(reports):
        return True
    for i in range(len(reports)):
        if part1(reports[:i] + reports[i+1:]):
            return True
    return False

def main():
    
    reports = [[int(x) for x in line.split()] for line in inFile]

    safe_count = sum(1 for report in reports if part1(report))
    
    safe_count2 = sum(1 for report in reports if part2(report))

    with open("day2/input.refout", "w") as outFile:
        outFile.write(str(safe_count) + "\n")
        outFile.write(str(safe_count2) + "\n")


if __name__ == "__main__":
    main()