import unittest
from task_322 import max_sum_dividers
from task_88a_b import is_3_in_nn, reverse_number


class TestTasks(unittest.TestCase):
    def test_task_332(self):
        self.assertEqual(max_sum_dividers(), 9240)

    def test_task_88a(self):
        self.assertTrue(is_3_in_nn(6))
        self.assertFalse(is_3_in_nn(7))

        with self.assertRaises(ValueError):
            is_3_in_nn('sdf')

    def test_task_88b(self):
        self.assertEqual(reverse_number(123), 321)
        self.assertEqual(reverse_number(1230), 321)

        with self.assertRaises(ValueError):
            is_3_in_nn('sdf')
            is_3_in_nn(123.3)
