class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            diagonal = 0
            for j in range(len(text2) - 1, -1, -1):
                oldCell = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + diagonal
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                diagonal = oldCell

        return dp[0]