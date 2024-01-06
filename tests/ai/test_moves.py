import unittest

import numpy as np
from ai.moves.bumpiness import bumpiness
from ai.moves.height import aggregate_height
from ai.moves.holes import holes
from ai.moves.lines import complete_lines


class TestFitness(unittest.TestCase):
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
