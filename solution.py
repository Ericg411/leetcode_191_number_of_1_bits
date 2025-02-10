class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_string = bin(n) [2:]
        counter = 0
        for c in binary_string:
            if c == '1':
                counter += 1
        return counter