import unittest

import numpy as np
from ai.heuristics import aggregate_height, bumpiness, complete_lines, holes


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

    def test_aggregate_height(self) -> None:
        self.assertEqual(aggregate_height(self.field), 48)

    def test_complete_lines(self) -> None:
        self.assertEqual(complete_lines(self.field), 2)

    def test_holes(self) -> None:
        self.assertEqual(holes(self.field), 2)

    def test_bumpiness(self) -> None:
        self.assertEqual(bumpiness(self.field), 6)
