import random
from itertools import permutations
from datetime import datetime
startTime = datetime.now()

solution = [
    [1, 4, 2, 3], 
    [2, 1, 3, 4], 
    [3, 2, 4, 1], 
    [4, 3, 1, 2]
]


def generate_solution(n):

    def is_valid(sq, row):
        for col in range(n):
            col_values = [sq[r][col] for r in range(len(sq))]
            if row[col] in col_values:
                return False
        return True

    symbols = list(range(1, n + 1))
    square = []

    def backtrack():
        if len(square) == n:
            return True

        random.shuffle(symbols)
        for perm in permutations(symbols):
            row = list(perm)
            if is_valid(square, row):
                square.append(row)
                if backtrack():
                    return True
                square.pop()
        return False

    backtrack()
    return square



def count_visible(buildings):
    max_seen = 0
    visible = 0
    for height in buildings:
        if height > max_seen:
            visible += 1
            max_seen = height
    return visible



def get_counters(r, c, right, left, top, bottom, sol):
    if r:
        if left:
            return [count_visible(row) for row in sol]
        elif right:
            return [count_visible(list(reversed(row))) for row in sol]
        else:
            return None
    elif c:
        columns = get_columns(sol)
        if top:
            return [count_visible(col) for col in columns]
        elif bottom:
            return [count_visible(list(reversed(col))) for col in columns]
        else:
            return None
    else:
        return None

def get_columns(buildings):
    cols = []
    for _ in range(len(buildings[0])):
        cols.append([])

    for i in range(len(buildings[0])):
        for j, row in enumerate(buildings):
            cols[i].append(row[i])
    return cols


def get_grid():
    final_grid = [get_counters(False, True, False, False, True, False, solution), get_counters(True, False, True, False, False, False, solution), get_counters(False, True, False, False, False, True, solution), get_counters(True, False, False, True, False, False, solution)]
    print(datetime.now() - startTime)
    print("Grid :", final_grid)
    return final_grid


def solve_grid(grid, n):
    sol = [[0] * n for _ in range(n)]
    for j in range(n):
        if grid[0][j] == n:
            for i in range(n):
                sol[i][j] = i + 1
        if grid[1][j] == n:
            for i in reversed(range(n)):
                sol[j][i] = n - i
        if grid[2][j] == n:
            for i in reversed(range(n)):
                sol[i][j] = n - i
        if grid[3][j] == n:
            for i in range(n):
                sol[j][i] = i + 1
        if grid[0][j] == 1:
            sol[0][j] = n
        if grid[1][j] == 1:
            sol[j][n -1] = n
        if grid[2][j] == 1:
            sol[3][j] = n
        if grid[3][j] == 1:
            sol[j][0] = n

    print(sol)




if __name__ == '__main__':
    while True:
        difficulty = int(input("Choose difficulty between 4 and 8: "))
        """solution = generate_solution(difficulty)"""
        """print(solution)"""
        solve_grid(get_grid(), difficulty)







