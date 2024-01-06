import unittest

import numpy as np
from ai.fitness.bumpiness import get_bumpiness
from ai.fitness.holes import holes
from ai.fitness.peaks import get_peaks_sum
from ai.fitness.transitions import (
    get_col_transition,
    get_row_transition,
)
from ai.fitness.wells import get_wells


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
            self.assertEqual(get_peaks_sum(field=field), answer)

    def test_get_row_transistions(self) -> None:
        answers = (8, 0, 2)
        for field, answer in zip(self.fields, answers):
            self.assertEqual(get_row_transition(field), answer)

    def test_get_col_transistions(self) -> None:
        answers = (5, 0, 1)
        for field, answer in zip(self.fields, answers):
            self.assertEqual(get_col_transition(field), answer)

    def test_get_bumpiness(self):
        answers = (5, 0, 4)
        for field, answer in zip(self.fields, answers):
            self.assertEqual(get_bumpiness(field=field), answer)

    def test_get_holes(self) -> None:
        answers = (
            np.array([1, 1, 0, 1, 2]),
            np.array([0, 0, 0, 0, 0]),
            np.array([0, 1, 0, 0, 0]),
        )
        for field, answer in zip(self.fields, answers):
            self.assertTrue(np.array_equal(holes(field), answer))

    def test_get_wells(self) -> None:
        answers = (
            np.array([1, 0, 2, 1, 0]),
            np.array([0, 0, 0, 0, 0]),
            np.array([2, 0, 2, 0, 0]),
        )
        for field, answer in zip(self.fields, answers):
            self.assertTrue(np.array_equal(get_wells(field=field), answer))
