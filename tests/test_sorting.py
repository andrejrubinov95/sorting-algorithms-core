import unittest
from sorting import bubble_sort, insertion_sort


class AlgorithmTests(unittest.TestCase):
    def test_bubble(self):
        self.assertEqual(bubble_sort([4, -2, 4, 0]), [-2, 0, 4, 4])

    def test_insertion(self):
        self.assertEqual(insertion_sort([9, 1, 2, -5]), [-5, 1, 2, 9])

    def test_does_not_mutate_source(self):
        value = [3, 1, 2]
        bubble_sort(value)
        insertion_sort(value)
        self.assertEqual(value, [3, 1, 2])

    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(insertion_sort([]), [])


if __name__ == '__main__':
    unittest.main()
