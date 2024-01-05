import unittest

import numpy as np
from ai.fitness.peaks import get_peaks


class TestFitness(unittest.TestCase):
    def test_get_peaks(self) -> None:
        field = np.array(
            [
                [0, 1, 0, 0, 1],
                [1, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
            ]
        )
        self.assertEqual(get_peaks(field), 11)

    def test_get_peaks_zeros(self) -> None:
        field = np.zeros((3, 5))
        self.assertEqual(get_peaks(field), 0)

    def test_single_peak(self):
        field = np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )

        self.assertEqual(get_peaks(field), 2)
