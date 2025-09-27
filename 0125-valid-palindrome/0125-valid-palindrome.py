class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        given_str = re.sub(r'[^a-z0-9]', '', s)
        reverse_str = given_str[::-1]
        return given_str == reverse_str

        