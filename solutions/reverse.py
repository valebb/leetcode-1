class Solution:
    def reverse(self, x: int) -> int:
        def split_n(n: int) -> [int, int]:
            temp = n/10
            return int(10*(round(temp - int(temp), 1))), int(temp)
        
        reversed_x = []
        while x != 0:
            digit, x = split_n(x)
            # print(digit, x)
            reversed_x.append(digit)
        
        new_x = sum([d*10**i for i, d in enumerate(reversed_x[::-1])])
        
        if abs(new_x) > 2**31 - 1:
            return 0
        if x < 0:
            return -new_x
        return new_x
