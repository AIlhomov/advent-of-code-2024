import re
inFile = open("day3/input.in", "r")


def part1(lst):
    findTxt = re.compile(r"mul\((\d+),(\d+)\)")

    
    justNumbers = [(int(x), int(y)) for x, y in findTxt.findall(lst)]
    for line in inFile:
        x = findTxt.findall(line)
        for match in x:
            justNumbers.append((int(match[0]), int(match[1])))
    
    
    res = 0
    for pair in justNumbers:
        res += pair[0] * pair[1]
    with open("day3/input.refout", "w") as outFile:
        outFile.write(str(res) + "\n")

def part2(lst):
    findTxt =  re.compile(r"mul\((\d+),(\d+)\)")

    enable = True
    res = 0

    i = 0
    while i < len(lst):
        if lst[i:i+4] == "do()":
            enable = True
            i += 4
        elif lst[i:i+7] == "don't()":
            enable = False
            i += 7
        else:
            match = findTxt.match(lst, i)
            if match and enable:
                x, y = int(match.group(1)), int(match.group(2))
                res += x * y
                i += len(match.group())
            else:
                i += 1
    with open("day3/input.refout", "a") as outFile:
        outFile.write(str(res) + "\n")

def main():
    

    file_content = inFile.read()
    part1(file_content)
    part2(file_content)

if __name__ == "__main__":
    main()