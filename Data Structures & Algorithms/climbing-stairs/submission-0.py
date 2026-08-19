class Solution:
    def climbStairs(self, n: int) -> int:
        current, previous = 1, 1
        for i in range(n-1):
            x = current
            current += previous
            previous = x
        return current