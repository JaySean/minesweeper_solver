import generator
import warnings
from scipy.optimize import linprog

warnings.filterwarnings("ignore")


def solve(m, n, minefield):

    def get_adj_cells(r, c):
        range_r, range_c = range(0, m), range(0, n)
        new_minefield = [0 for _ in range(m*n)]
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                new_r, new_c = r + dr, c + dc
                if new_r in range_r and new_c in range_c:
                    new_minefield[new_r*n + new_c] = 1
        return new_minefield

    lhs_eq = [get_adj_cells(row, col) for row in range(m) for col in range(n)]
    rhs_eq = [cell for row in minefield for cell in row]

    obj = [1 for _ in range(m*n)]
    bnd = [(0, 1) for _ in range(m*n)]
    opt = linprog(c=obj, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd)

    return opt.x.round().astype(int)


def main():
    f = open('input.txt', "r")

    # Read in parameters (m, n, x)
    params = list(map(int, f.readline().split()))
    assert(len(params) == 3), "Wrong number of parameters"
    m, n, x = params

    # Read in minefield
    minefield = [line.split() for line in f.read().splitlines()]
    assert(m == len(minefield)), "Wrong number of rows"
    assert(all(n == len(row) for row in minefield)), "Wrong number of cols"

    # Solve
    mines = solve(m, n, minefield)
    output = generator.generate_output(m, n, mines)

    # Print output and write output to file
    f = open('output.txt', "w")
    f.write(output)
    print(output)


if __name__ == "__main__":
    main()
