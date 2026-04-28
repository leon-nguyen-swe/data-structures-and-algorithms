# LeetCode 3271. Hash Divided String

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        
        res = []
        for i in range(0, n, k):
            curSum = 0
            for j in range(i, i + k):
                curSum += ord(s[j]) - ord('a')
            res.append(chr(curSum % 26 + ord('a')))

        return "".join(res)