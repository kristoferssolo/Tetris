import unittest

import numpy as np
from ai.fitness.peaks import get_peaks_sum
from ai.fitness.transitions import (
    get_col_transition,
    get_col_transitions2,
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
            self.assertEqual(get_peaks_sum(field), answer)

    def test_get_row_transistions(self):
        answers = (8, 0, 2)
        for field, answer in zip(self.fields, answers):
            self.assertEqual(get_row_transition(field), answer)

    def test_get_col_transistions2(self):
        answers = (5, 0, 1)
        for field, answer in zip(self.fields, answers):
            self.assertEqual(get_col_transition(field), answer)