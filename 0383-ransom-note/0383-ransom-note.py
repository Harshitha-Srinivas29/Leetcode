class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if sorted(ransomNote) in sorted(magazine):
            return True
        return False
        