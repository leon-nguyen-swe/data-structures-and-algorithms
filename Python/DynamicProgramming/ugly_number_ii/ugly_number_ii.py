# LeetCode 264. Ugly Number II

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        i2 = i3 = i5 = 0

        for i in range(1, n):
            n2 = dp[i2] * 2
            n3 = dp[i3] * 3
            n5 = dp[i5] * 5

            dp[i] = min(n2, n3, n5)

            if dp[i] == n2:
                i2 += 1
            if dp[i] == n3:
                i3 += 1
            if dp[i] == n5:
                i5 += 1
        
        return dp[n-1]