import unittest
import random_game_testing


class TestGame(unittest.TestCase):
  #1
    def test_input(self):
        answer = 5
        guess = 5
        result = random_game_testing.run_guess(answer, guess)
        self.assertTrue(result)
  #2
    def test_input(self):
        result = random_game_testing.run_guess(5,5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = random_game_testing.run_guess(5,0)
        self.assertFalse(result)
#3
    def test_input_wrong_number(self):
        result = random_game_testing.run_guess(5,12)
        self.assertFalse(result)
#4
    def test_input_wrong_type(self):
        result = random_game_testing.run_guess(5,'12')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
