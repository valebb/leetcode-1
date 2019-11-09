from unittest import TestCase
from solutions.add_binary import Solution


class TestAddBinary(TestCase):
    def test_example_1(self):
        a = "11"
        b = "1"
        expected = "100"

        print(Solution().addBinary(a, b))

        self.assertEqual(
            expected,
            Solution().addBinary(a, b)
        )

    def test_example_2(self):
        a = "1010"
        b = "1011"
        expected = "10101"

        self.assertEqual(
            expected,
            Solution().addBinary(a, b)
        )

    def test_addBinaryCharacters(self):
        self.assertEqual(
            ('0', True),
            Solution.addBinaryCharacters('1', '1', False)
        )

        self.assertEqual(
            ('1', True),
            Solution.addBinaryCharacters('1', '1', True)
        )


