inFile = open("day4/input.in", "r")

def vertically_diagonal(word, row, col, direction, grid):
    m = len(grid)
    if not m:
        return False
    
    n = len(grid[0])
    if not n:
        return False
    
    directions = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1),
        "up_right": (-1, 1), # diagonals
        "down_right": (1, 1),
        "down_left": (1, -1),
        "up_left": (-1, -1)
    }
    if direction not in directions:
        return False
    i = 0
    r, c = row, col

    while i < len(word) and 0 <= r < m and 0 <= c < n:
        if grid[r][c] != word[i]:
            return False
        r += directions[direction][0]
        c += directions[direction][1]
        i += 1
    if i == len(word):
        print(f"{word} found at ({row}, {col}) going {direction}")

    return i == len(word)

def part1(file_line):
    grid = [list(line.strip()) for line in file_line]

    res = 0

    directions = ["right", "down", "up", "left", "up_right", "down_right", "down_left", "up_left"]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for direction in directions:
                if vertically_diagonal("XMAS", row, col, direction, grid):
                    res += 1
    with open("day4/input.refout", "w") as outFile:
        outFile.write(str(res) + "\n")
def part2(file_line):

    grid = [list(line.strip()) for line in file_line]

    res = 0
    
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):

            if grid[row][col] == 'A': #Checks the center of the grid
                d1 = grid[row-1][col-1] + grid[row+1][col+1] #Diagonal 1
                d2 = grid[row-1][col+1] + grid[row+1][col-1]


                if (d1 == 'MS' or d1 == 'SM') and (d2 == 'MS' or d2 == 'SM'):
                    res += 1
        
    with open("day4/input.refout", "a") as outFile:
        outFile.write(str(res) + "\n")
    #print(res)

def main():
    file_line = inFile.readlines()

    part1(file_line)
    part2(file_line)

if __name__ == "__main__":
    main()