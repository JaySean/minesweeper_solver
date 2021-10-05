import unittest
import generator
import solver
import warnings

warnings.filterwarnings("ignore")


class TestSolver(unittest.TestCase):
    def test_beginner(self):
        m, n, x = 9, 9, 10
        generated_mines = generator.generate_mines(m, n, x)
        generated_minefield = generator.generate_minefield(m, n, generated_mines)
        solved_answer = solver.solve(m, n, generated_minefield)
        solved_mines = [i for i in range(m * n) if solved_answer[i] == 1]

        self.assertEqual(generated_mines, solved_mines)

    def test_intermediate(self):
        m, n, x = 16, 16, 40
        generated_mines = generator.generate_mines(m, n, x)
        generated_minefield = generator.generate_minefield(m, n, generated_mines)
        solved_answer = solver.solve(m, n, generated_minefield)
        solved_mines = [i for i in range(m * n) if solved_answer[i] == 1]

        self.assertEqual(generated_mines, solved_mines)

    def test_expert(self):
        m, n, x = 30, 16, 99
        generated_mines = generator.generate_mines(m, n, x)
        generated_minefield = generator.generate_minefield(m, n, generated_mines)
        solved_answer = solver.solve(m, n, generated_minefield)
        solved_mines = [i for i in range(m * n) if solved_answer[i] == 1]

        self.assertEqual(generated_mines, solved_mines)


if __name__ == '__main__':
    unittest.main()
