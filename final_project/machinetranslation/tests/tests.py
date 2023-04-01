import unittest
from translator import frenchToEnglish, englishToFrench

class TestFrenchToEnglish(unittest.TestCase):
    def test_translation(self):
        result = frenchToEnglish('Bonjour')
        expected = 'Hello'
        self.assertEqual(result, expected)

    def test_null_input(self):
        result = frenchToEnglish(None)
        expected = None
        self.assertEqual(result, expected)

class TestEnglishToFrench(unittest.TestCase):
    def test_translation(self):
        result = englishToFrench('Hello')
        expected = 'Bonjour'
        self.assertEqual(result, expected)

    def test_null_input(self):
        result = englishToFrench(None)
        expected = None
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()