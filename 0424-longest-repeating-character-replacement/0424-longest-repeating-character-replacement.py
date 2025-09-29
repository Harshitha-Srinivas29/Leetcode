class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        count = [0] * 26

        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            while (right-left + 1) -max(count) > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            result = max(result, right-left + 1)
        return result