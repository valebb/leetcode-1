from typing import Tuple

binary_character_outcomes = {
    ("0", "0"): ("0", False),
    ("1", "0"): ("1", False),
    ("0", "1"): ("1", False),
    ("1", "1"): ("0", True)
}


class Solution:

    # Super fast best solution, but feels like cheating using the built-ins
    # def addBinary(self, a: str, b: str) -> str:
    #     output_decimal = int(a, 2) + int(b, 2)
    #     return "{:b}".format(output_decimal)

    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            xs = a[::-1]
            ys = b[::-1]
        else:
            xs = b[::-1]
            ys = a[::-1]

        output = ""
        remainder = False
        i = 0
        while i < len(ys):
            ch, remainder = self.addBinaryCharacters(xs[i], ys[i], remainder)
            output += ch
            i += 1

        while i < len(xs):
            ch, remainder = self.addBinaryCharacters(xs[i], '0', remainder)
            output += ch
            i += 1

        if remainder:
            output += "1"

        return output[::-1]

    @staticmethod
    def addBinaryCharacters(
            a: str, b: str, remainder: bool = False) -> Tuple[str, bool]:
        """Returns string value and whether there is remainder"""
        s, rem = binary_character_outcomes[(a, b)]
        if remainder:
            s2, rem2 = binary_character_outcomes[(s, '1')]
            return s2, True if rem else rem2
        return s, rem
