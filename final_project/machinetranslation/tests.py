import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test_1(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish(None),None)
        self.assertEqual(frenchToEnglish(''),'')
        self.assertNotEqual(frenchToEnglish('Rouge'), 'Green')

    def test_2(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench(None),None)
        self.assertEqual(englishToFrench(''),'')
        self.assertNotEqual(englishToFrench('Green'), 'Rouge')

if __name__=='__main__':
    unittest.main()