import unittest
import statistics


def calculate_stats(data):
    if not data:
        raise ValueError("Input list cannot be empty")

    mean = sum(data) / len(data)
    median = statistics.median(data)
    std_dev = statistics.stdev(data)

    return mean, median, std_dev


class TestCalculateStats(unittest.TestCase):

    def test_mean_median_stddev(self):
        data = [2, 4, 6, 8, 10]
        mean, median, std_dev = calculate_stats(data)
        self.assertAlmostEqual(mean, 6.0, places=2)
        self.assertEqual(median, 6)
        self.assertAlmostEqual(std_dev, 2.83, places=2)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_stats([])

    def test_single_element(self):
        data = [5]
        mean, median, std_dev = calculate_stats(data)
        self.assertEqual(mean, 5)
        self.assertEqual(median, 5)
        self.assertEqual(std_dev, 0)

    def test_negative_numbers(self):
        data = [-3, -1, 0, 2, 4]
        mean, median, std_dev = calculate_stats(data)
        self.assertAlmostEqual(mean, 0.4, places=2)
        self.assertEqual(median, 0)
        self.assertAlmostEqual(std_dev, 2.8, places=2)


if __name__ == '__main__':
    unittest.main()
