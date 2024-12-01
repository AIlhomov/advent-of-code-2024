inFile = open("day1/input.in", "r")

def part1(minList, maxList):
    # Sort the list first.
    # Then we just iterate through the list and get the absolute difference 
    # between the element in minList and maxList
    minList.sort()
    maxList.sort()
    
    ans = 0

    for i in range(len(minList)):
        ans += abs(minList[i] - maxList[i])

    with open("day1/input.refout", "w") as outFile:
        outFile.write(str(ans) + "\n")

def part2(leftList, rightList):
    # Just a simple nested loop to find the common occurences for 1 element in 
    # leftList and all element in rightList.
    # Then after that we just multiply the element in leftList with the occurences found
    res = 0
    occurences = 0
    for num1 in leftList:
        for num2 in rightList:
            if num1 == num2:
                occurences += 1
        res += num1 * occurences
        occurences = 0
    with open("day1/input.refout", "a") as outFile:
        outFile.write(str(res) + "\n")

    
    

def main():
    lines = inFile.readlines()
    inFile.close()

    leftList = []
    rightList = []

    for line in lines:
        num1, num2 = map(int, line.strip().split())
        leftList.append(num1)
        rightList.append(num2)
    
    part1(leftList, rightList) # 1
    part2(leftList, rightList) # 2


if __name__ == "__main__":
    main()