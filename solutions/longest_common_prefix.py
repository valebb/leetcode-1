from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        output = ""
        shortest_length = min([len(s) for s in strs])
        for i in range(shortest_length):
            letters = set()
            for s in strs:
                letters.add(s[i])
            if len(letters) > 1:
                return output
            else:
                output += s[i]

        return output
