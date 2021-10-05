# Minesweeper Solver

## Description
### Problem
Given a table of cells, with each number representing the number of mines on itself and its neighbors, find out where the mines could be located.
```text
          0       1       2       3                       0       1       2       3
      ________________________________                ________________________________
      |       |       |       |       |               |       |       |       |       |
  0   |   1   |   2   |   3   |   2   |           0   |   0   |   0   |   0   |   *   |
      |_______|_______|_______|_______|               |_______|_______|_______|_______|
      |       |       |       |       |               |       |       |       |       |
  1   |   2   |   4   |   6   |   4   |           1   |   0   |   *   |   *   |   0   |
      |_______|_______|_______|_______|    ==>        |_______|_______|_______|_______|
      |       |       |       |       |    ==>        |       |       |       |       |
  2   |   2   |   4   |   5   |   3   |           2   |   0   |   *   |   *   |   *   |
      |_______|_______|_______|_______|               |_______|_______|_______|_______|
      |       |       |       |       |               |       |       |       |       |
  3   |   1   |   2   |   3   |   2   |           3   |   0   |   0   |   0   |   0   |
      |_______|_______|_______|_______|               |_______|_______|_______|_______|
```

## Solution
- Each cell in the minefield can be expressed as a linear equation involving its 8 neighbours and itself.
- A cell in row a col b is represented by the variable x<sub>ab</sub>
- Take for example the cell in row 1 col 2.  It corresponds to the equation:
  - x<sub>12</sub> = x<sub>01</sub> + x<sub>02</sub> + x<sub>03</sub> + x<sub>11</sub> + x<sub>12</sub> + x<sub>13</sub> + x<sub>21</sub> + x<sub>22</sub> + x<sub>23</sub> = 6
- scipy.optimize.linprog will take in the m * n equations and solve for the m * n cells

## Setup
```
git clone https://github.com/JaySean/minesweeper_solver.git
cd minesweeper_solver
pip install -r requirements.txt
```

## Usage
Place input data in input.txt
```
python3 solver.py
```
Output will be printed in the terminal and saved to output.txt

## Test Cases
```
python3 test_solver.py
```
Testing covers 3 common minesweeper levels:

| \#  | LEVEL    | ROWS | COLS | MINES |
| --- | -------- | ---- | ---- | ----- |
|  1  | Beginner | 9 | 9 | 10 |
|  1  | Intermediate | 16 | 16 | 40 |
|  1  | Expert | 30 | 16 | 99 |