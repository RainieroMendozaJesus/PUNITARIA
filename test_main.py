import unittest
from Hola import hola_mundo

class TestHolaMundo(unittest.TestCase):
    def test_hola_mundo(self):
        self.assertEqual(hola_mundo(), "Hola Mundo")

if __name__ == "__main__":
    unittest.main()
