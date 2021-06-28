import unittest

from instruments import get_country_code


class GetCountryCodeTestCase(unittest.TestCase):
    """Класс для тестирования функции get_country_code."""
    
    def test_get_country_code_ru(self):
        """Тест для Russian Federation"""
        self.country_name = 'Russian Federation'
        self.assertEqual(get_country_code(self.country_name), 'ru')

    def test_get_country_code_vietnam(self):
        """Тест для Russian Federation"""
        self.country_name = 'Vietnam'
        self.assertEqual(get_country_code(self.country_name), 'vn')
  
        
if __name__ == '__main__':
    unittest.main()
