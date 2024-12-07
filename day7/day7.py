from itertools import product

def evaluate_expression(numbers, operators):
    res = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            res += numbers[i + 1]
        elif op == '*':
            res *= numbers[i + 1]
    return res

def can_solve_equation(target, numbers):
    num_operators = len(numbers) - 1
    for operators in product(['+', '*'], repeat=num_operators):
        if evaluate_expression(numbers, operators) == target:
            return True
    return False

def parse_input(lines):
    equations = []
    for line in lines:
        target, *numbers = map(int, line.replace(':', '').split())
        equations.append((target, numbers))
    return equations

def main():
    with open("day7/input.in", "r") as file:
        lines = file.readlines()

    equ = parse_input(lines)

    tot = 0
    for target, num in equ:
        if can_solve_equation(target, num):
            tot += target
    with open("day7/input.refout", "w") as outFile:
        outFile.write(str(tot) + "\n")
    print(tot)

if __name__ == "__main__":
    main()
