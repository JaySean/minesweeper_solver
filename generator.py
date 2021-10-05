import random


def generate_mines(m, n, x):
    mines = sorted(random.sample(range(m * n), x))
    return mines


def generate_minefield(m, n, mines):
    minefield = [[0 for _ in range(n)] for _ in range(m)]
    range_r, range_c = range(0, m), range(0, n)

    for mine in mines:
        r, c = mine // n, mine % n
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                new_r, new_c = r + dr, c + dc
                if new_r in range_r and new_c in range_c:
                    minefield[new_r][new_c] += 1
    return minefield


def generate_output(m, n, mines):
    minefield = [['0' for _ in range(n)] for _ in range(m)]
    for i, mine in enumerate(mines):
        if mine == 1:
            r, c = i // n, i % n
            minefield[r][c] = '*'

    return '\n'.join([' '.join(row) for row in minefield])

