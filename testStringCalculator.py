import unittest
from unittest.mock import MagicMock
from stringCalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.logger = MagicMock();
        self.stringCalculator = StringCalculator(self.logger);

    def test_add_empty_string(self):
        self.assertEqual(self.stringCalculator.add(""), 0);

    def test_add_one_number(self):
        self.assertEqual(self.stringCalculator.add("1"), 1);

    def test_add_mutilple_numbers(self):
        self.assertEqual(self.stringCalculator.add("1,2"), 3);
        self.assertEqual(self.stringCalculator.add("1,2,5,10,0"), 18);

    def test_add_new_lines(self):
        self.assertEqual(self.stringCalculator.add("1\n2,3"), 6);

    def test_add_change_delimeter(self):
        self.assertEqual(self.stringCalculator.add("//;\n1;2"), 3);
        self.assertEqual(self.stringCalculator.add("//;\n1;20"), 21);

    def test_add_negatives_not_allowed(self):
        with self.assertRaises(Exception)as cm :
            self.stringCalculator.add("1,-2");
        self.assertEqual("negatives not allowed: -2", cm.exception.args[0]);
        with self.assertRaises(Exception)as cm :
            self.stringCalculator.add("1,-2,-10");
        self.assertEqual("negatives not allowed: -2 -10", cm.exception.args[0])

    def test_add_numbers_bigger_than_1000(self):
        self.assertEqual(self.stringCalculator.add("1000, 2"), 2);

    def test_add_any_length_delimeter(self):
        self.assertEqual(self.stringCalculator.add("//[***]\n1***2***3"), 6);

    def test_add_mutilple_delimeter(self):
        self.assertEqual(self.stringCalculator.add("//[***][;]\n1***2;3"), 6);

    def test_logger(self):
        self.stringCalculator.add("1,2");
        self.logger.write.assert_called_once_with("3");

    def test_logger_with_exception(self):
        self.logger.write.side_effect = Exception("logging has failed")
        self.assertEqual(self.stringCalculator.add("1,2"), "logging has failed")

if __name__ == '__main__':
    unittest.main()
