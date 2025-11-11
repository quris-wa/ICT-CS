"""Тесты для проверки работы функций решателя судоку"""
import io
import os
import tempfile
import textwrap
import unittest

from src.lab3.sudoku import (group, create_grid, read_sudoku, display, get_row, get_col, get_block,
                             find_empty_positions, find_possible_values, solve, check_solution, generate_sudoku)


class SudokuTestCase(unittest.TestCase):

    def test_group_basic(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(
            group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3),
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        )

    def test_group_invalid_n_raises(self):
        with self.assertRaises(ValueError):
            group([1, 2, 3], 0)
        with self.assertRaises(ValueError):
            group([1, 2, 3], -3)

    def test_create_grid(self):
        raw = "53..7....\n6..195...\n.98....6.\n"
        grid = create_grid(raw)
        # Только допустимые символы и разбиение на строки по 9
        self.assertEqual(len(grid), 3)
        self.assertTrue(all(len(row) == 9 for row in grid))
        self.assertEqual(grid[0][:5], ["5", "3", ".", ".", "7"])

    def test_read_sudoku_from_tempfile(self):
        content = textwrap.dedent(
            """
            53..7....
            6..195...
            .98....6.
            8...6...3
            4..8.3..1
            7...2...6
            .6....28.
            ...419..5
            ....8..79
            """
        ).strip()
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "puzzle.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            grid = read_sudoku(path)
        self.assertEqual(len(grid), 9)
        self.assertTrue(all(len(row) == 9 for row in grid))
        self.assertEqual(grid[0][0], "5")
        self.assertEqual(grid[0][1], "3")
        self.assertEqual(grid[0][2], ".")


    def test_get_row(self):
        grid = [["1", "2", "."], ["4", ".", "6"], [".", "8", "9"]]
        self.assertEqual(get_row(grid, (0, 0)), ["1", "2", "."])
        self.assertEqual(get_row(grid, (1, 2)), ["4", ".", "6"])
        self.assertEqual(get_row(grid, (2, 1)), [".", "8", "9"])

    def test_get_col(self):
        grid = [["1", "2", "."], ["4", ".", "6"], [".", "8", "9"]]
        self.assertEqual(get_col(grid, (0, 0)), ["1", "4", "."])
        self.assertEqual(get_col(grid, (0, 1)), ["2", ".", "8"])
        self.assertEqual(get_col(grid, (0, 2)), [".", "6", "9"])

    def test_get_block(self):
        grid = create_grid(
            "53..7....\n6..195...\n.98....6.\n"
            "8...6...3\n4..8.3..1\n7...2...6\n"
            ".6....28.\n...419..5\n....8..79\n"
        )
        self.assertEqual(
            get_block(grid, (0, 1)),
            ["5", "3", ".", "6", ".", ".", ".", "9", "8"],
        )
        self.assertEqual(
            get_block(grid, (4, 7)),
            [".", ".", "3", ".", ".", "1", ".", ".", "6"],
        )
        self.assertEqual(
            get_block(grid, (8, 8)),
            ["2", "8", ".", ".", ".", "5", ".", "7", "9"],
        )


    def test_find_empty_positions(self):
        self.assertEqual(
            find_empty_positions([["1", "2", "."], ["4", "5", "6"], ["7", "8", "9"]]),
            (0, 2),
        )
        self.assertEqual(
            find_empty_positions([["1", "2", "3"], ["4", ".", "6"], ["7", "8", "9"]]),
            (1, 1),
        )
        self.assertEqual(
            find_empty_positions([["1", "2", "3"], ["4", "5", "6"], [".", "8", "9"]]),
            (2, 0),
        )
        self.assertIsNone(
            find_empty_positions([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
        )

    def test_find_possible_values(self):
        grid = create_grid(
            "53..7....\n6..195...\n.98....6.\n"
            "8...6...3\n4..8.3..1\n7...2...6\n"
            ".6....28.\n...419..5\n....8..79\n"
        )
        values = find_possible_values(grid, (0, 2))
        self.assertEqual(values, {"1", "2", "4"})
        values = find_possible_values(grid, (4, 7))
        self.assertEqual(values, {"2", "5", "9"})


    def test_check_solution_false_on_bad_board(self):
        bad = [
            ["5", "5", "4", "6", "7", "8", "9", "1", "2"],  # повтор 5 в строке
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        self.assertFalse(check_solution(bad))


    def test_generate_sudoku_counts_and_solve(self):
        # N=40 - 41 пустая клетка
        grid = generate_sudoku(40)
        empties = sum(1 for row in grid for e in row if e == ".")
        self.assertEqual(empties, 81 - 40)
        solved = solve([row[:] for row in grid])
        self.assertIsNotNone(solved)
        self.assertTrue(check_solution(solved))

        # N=1000 - все заполнено
        grid_full = generate_sudoku(1000)
        empties_full = sum(1 for row in grid_full for e in row if e == ".")
        self.assertEqual(empties_full, 0)
        self.assertTrue(check_solution(grid_full))

        # N=0  - все пусто, но решаемо
        grid_empty = generate_sudoku(0)
        empties_zero = sum(1 for row in grid_empty for e in row if e == ".")
        self.assertEqual(empties_zero, 81)
        solved_zero = solve(grid_empty)
        self.assertIsNotNone(solved_zero)
        self.assertTrue(check_solution(solved_zero))


if __name__ == "__main__":
    unittest.main()
