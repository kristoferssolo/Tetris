import unittest

import numpy as np
from ai.fitness.bumpiness import get_bumpiness
from ai.fitness.peaks import get_peaks_sum
from ai.fitness.transitions import (
    get_col_transition,
    get_row_transition,
)


class TestFitness(unittest.TestCase):
    def setUp(self) -> None:
        self.fields: tuple[np.ndarray] = (
            np.array(
                [
                    [0, 1, 0, 0, 1],
                    [1, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                ]
            ),
            np.zeros((3, 5)),
            np.array(
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ]
            ),
        )

    def test_get_peaks_sum(self) -> None:
        answers: tuple[int] = (11, 0, 2)
        for field, answer in zip(self.fields, answers):
            self.assertEqual(get_peaks_sum(None, field), answer)

    def test_get_row_transistions(self):
        answers = (8, 0, 2)
        for field, answer in zip(self.fields, answers):
            self.assertEqual(get_row_transition(field), answer)

    def test_get_col_transistions(self):
        answers = (5, 0, 1)
        for field, answer in zip(self.fields, answers):
            self.assertEqual(get_col_transition(field), answer)

    def test_get_bumpiness(self):
        answers = (5, 0, 4)
        for field, answer in zip(self.fields, answers):
            self.assertEqual(get_bumpiness(None, field), answer)

    def test_get_holes(self):
        answers = (
            np.array([1, 1, 0, 1, 2]),
            np.array([0, 0, 0, 0, 0]),
            np.array([0, 1, 0, 0, 0]),
        )
        for field, answer in zip(self.fields, answers):
            self.assertTrue(np.array_equal(get_holes(field), answer))
