class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        inputStr = re.sub(r'[^a-z0-9]', '',s)
        reversedStr = inputStr[::-1]
        return reversedStr == inputStr
