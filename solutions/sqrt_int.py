from typing import Set


class Solution:

    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        min_i = 0
        max_i = x
        checked = set()
        max_allowed = 1

        while True:
            mid_i = min_i + (max_i - min_i) // 2

            sq = mid_i ** 2
            if sq == x:
                return mid_i
            elif mid_i in checked:
                return max_allowed
            elif sq < x:
                if mid_i > max_allowed:
                    max_allowed = mid_i
                min_i = mid_i
                checked.add(mid_i)
                continue
            elif sq > x:
                max_i = mid_i
                checked.add(mid_i)
                continue
            else:
                raise RuntimeError

    # Cheating
    # def mySqrt(self, x: int) -> int:
    #     return int(x ** (1/2))

    # Time limit exceeded
    # def mySqrt(self, x: int) -> int:
    #     if x < 2:
    #         return x
    #
    #     for i in range(x + 1):
    #         if (i ** 2) <= x:
    #             continue
    #         return i - 1

    # Still too slow
    # def mySqrt(self, x: int) -> int:
    #     if x < 2:
    #         return x
    #
    #     def rec(min_i: int, max_i: int, allowed: Set[int], checked: Set[int]):
    #         mid_i = min_i + (max_i - min_i) // 2
    #         sq = (mid_i ** 2)
    #         print(min_i, max_i, mid_i)
    #         if mid_i in checked:
    #             return max(allowed)
    #         if sq < x:
    #             return rec(mid_i, max_i, allowed.union({mid_i}), checked.union({mid_i}))
    #         elif sq > x:
    #             return rec(min_i, mid_i, allowed, checked.union({mid_i}))
    #         else:
    #             return mid_i
    #
    #     return rec(0, x, set(), set())
