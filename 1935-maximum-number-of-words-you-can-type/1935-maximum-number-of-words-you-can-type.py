class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0
        for word in words:
            if not any(c in brokenLetters for c in word):
                count += 1
        return count