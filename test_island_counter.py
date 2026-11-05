import unittest
from island_counter import island_sizes


class IslandCounterTests(unittest.TestCase):
    def test_empty_grid(self):
        self.assertEqual(island_sizes([]), [])
        self.assertEqual(island_sizes([[]]), [])

    def test_all_water(self):
        self.assertEqual(island_sizes([[0, 0], [0, 0]]), [])

    def test_one_island(self):
        self.assertEqual(island_sizes([[1, 1], [0, 1]]), [3])

    def test_diagonal_cells_are_separate(self):
        self.assertEqual(island_sizes([[1, 0], [0, 1]]), [1, 1])

    def test_sample_grid(self):
        grid = [
            [1, 1, 0, 0, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 1],
        ]
        self.assertEqual(island_sizes(grid), [4, 2, 2, 3, 2, 2])


if __name__ == "__main__":
    unittest.main()

