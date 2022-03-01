import unittest
import HW05_Jdesai_Wordle

class wordle_test(unittest.TestCase):

    def test_get_init(self):
            result = HW05_Jdesai_Wordle.get_init()
            self.assertEqual(result)

    def test_get_word(self):
            result = HW05_Jdesai_Wordle.get_word()
            self.assertEqual(result)

    def test_get_user_input(self):
            result = HW05_Jdesai_Wordle.has_user_guessed_the_right_word()
            self.assertEqual(result)

    def test_check_if_entered_word_is_valid(self):
            result = HW05_Jdesai_Wordle.check_if_entered_word_is_valid()
            self.assertEqual(result)

    def test_user_guessed_the_right_word(self):
            result = HW05_Jdesai_Wordle.has_user_guessed_the_right_word()
            self.assertEqual(result)

    def test_check_valid_word(self):
            result = HW05_Jdesai_Wordle.check_if_entered_word_is_valid()
            self.assertEqual(result)

    def test_get_spot_name(self):
            result = HW05_Jdesai_Wordle.get_spot_name()
            self.assertEqual(result)

    def test_check_word_in_dictionary(self):
            result = HW05_Jdesai_Wordle.check_if_word_in_dictionary()
            self.assertEqual(result)

    def test_get_final(self):
            result = HW05_Jdesai_Wordle.get_spot_name()
            self.assertEqual(result)

if __name__ == '__main__':
            unittest.main()