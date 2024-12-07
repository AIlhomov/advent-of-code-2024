def parse_input(grid):
    """Find the guard's starting position"""
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    guard_pos = None
    guard_dir = None

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                guard_pos = (r, c)
                guard_dir = directions[cell]
                grid[r][c] = '.'
                break
        if guard_pos:
            break

    return grid, guard_pos, guard_dir

def turn_right(direction):
    """Turn 90 degrees to the right."""
    turns = {
        (-1, 0): (0, 1),  # Up -> Right
        (0, 1): (1, 0),   # Right -> Down
        (1, 0): (0, -1),  # Down -> Left
        (0, -1): (-1, 0)  # Left -> Up
    }
    return turns[direction]

def simulate(grid, guard_pos, guard_dir):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    while True:
        visited.add(guard_pos)
        r, c = guard_pos

        dr, dc = guard_dir
        nr, nc = r + dr, c + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            break

        if grid[nr][nc] == '#':
            guard_dir = turn_right(guard_dir)
        else:
            guard_pos = (nr, nc)

    return len(visited)

def part1(grid):
    grid, guard_pos, guard_dir = parse_input(grid)
    return simulate(grid, guard_pos, guard_dir)

def main():
    with open("day6/input.in", "r") as inFile:
        grid = [list(line.strip()) for line in inFile]
        result = part1(grid)
        print(result)
    with open("day6/input.refout", "w") as outFile:
        outFile.write(str(result) + "\n")
        
if __name__ == "__main__":
    main()
