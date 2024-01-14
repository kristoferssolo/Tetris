import unittest

import numpy as np
from ai.heuristics import aggregate_height, complete_lines, count_holes, get_bumpiness


class TestHeuristics(unittest.TestCase):
    def setUp(self) -> None:
        self.field = np.array(
            [
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                [0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ]
        )

        self.field2 = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                [1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            ]
        )
        self.field3 = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            ]
        )

    def test_aggregate_height(self) -> None:
        self.assertEqual(aggregate_height(self.field), 48)
        self.assertEqual(aggregate_height(self.field2), 12)
        self.assertEqual(aggregate_height(self.field3), 30)

    def test_complete_lines(self) -> None:
        self.assertEqual(complete_lines(self.field), 2)
        self.assertEqual(complete_lines(self.field2), 0)
        self.assertEqual(complete_lines(self.field3), 1)

    def test_holes(self) -> None:
        self.assertEqual(count_holes(self.field), 2)
        self.assertEqual(count_holes(self.field2), 0)
        self.assertEqual(count_holes(self.field3), 2)

    def test_bumpiness(self) -> None:
        self.assertEqual(get_bumpiness(self.field), 6)
        self.assertEqual(get_bumpiness(self.field2), 11)
        self.assertEqual(get_bumpiness(self.field3), 7)
