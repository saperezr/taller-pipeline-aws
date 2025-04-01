import unittest
import funtions as f

class TestHeroes(unittest.TestCase):
    def test_load_file(self):
        data = f.load_file('./heroes.csv')
        self.assertEqual(len(data), 734)

if __name__ == "__main__":
    unittest.main()