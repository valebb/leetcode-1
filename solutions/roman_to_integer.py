# https://leetcode.com/problems/roman-to-integer/submissions/

raw_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution:
    def sliding_window_generator(self, s: str):
        for i in range(len(s) - 1):
            yield (
                raw_values[s[i]],
                raw_values[s[i + 1]]
            )
        yield (raw_values[s[-1]], 0)

    def romanToInt(self, s: str) -> int:
        output = 0
        modifier = 0

        for a, b in self.sliding_window_generator(s):
            if a < b:
                modifier = a
            else:
                output += a - modifier
                modifier = 0
        return output

