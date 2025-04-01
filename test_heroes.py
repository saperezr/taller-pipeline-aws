import unittest
from application import application
import funtions as f

class TestHeroesAPI(unittest.TestCase):
    def setUp(self):
        self.app = application.test_client()
        self.app.testing = True
        self.data = f.load_file('./heroes.csv')

    def test_load_file(self):
        """Test that the data loading function works correctly"""
        data = f.load_file('./heroes.csv')
        self.assertIsInstance(data, dict)
        self.assertTrue(len(data) > 0)
        
        # Test structure of first record
        first_key = list(data.keys())[0]
        first_record = data[first_key]
        self.assertIn('name', first_record)
        self.assertIn('gender', first_record)
        self.assertIn('eye_color', first_record)
        self.assertIn('race', first_record)
        self.assertIn('hair_color', first_record)
        self.assertIn('height', first_record)
        self.assertIn('publisher', first_record)
        self.assertIn('skin_color', first_record)
        self.assertIn('alignment', first_record)
        self.assertIn('weight', first_record)

    def test_index_route(self):
        """Test the main route returns all heroes"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), dict)
        self.assertEqual(response.get_json(), self.data)

    def test_heroe_route(self):
        """Test the individual hero route returns correct data"""
        # Get first hero ID from data
        first_hero_id = list(self.data.keys())[0]
        
        response = self.app.get(f'/{first_hero_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), self.data[first_hero_id])

    def test_invalid_heroe_route(self):
        """Test that invalid hero ID returns 404"""
        response = self.app.get('/invalid_id')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main() 