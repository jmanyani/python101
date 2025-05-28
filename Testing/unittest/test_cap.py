import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        self.assertEqual(cap.cap_text('python'), 'Python')

    def test_multiple_words(self):
        self.assertEqual(cap.cap_text('monty python'), 'Monty Python')

    def test_with_apostrophes(self):
        self.assertEqual(cap.cap_text("monty python's flying circus"), "Monty Python's Flying Circus")

if __name__ == '__main__':
    unittest.main()
