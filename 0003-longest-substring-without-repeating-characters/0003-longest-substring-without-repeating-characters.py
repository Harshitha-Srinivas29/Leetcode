class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_count = max(max_count, right-left+1)
        return max_count


        