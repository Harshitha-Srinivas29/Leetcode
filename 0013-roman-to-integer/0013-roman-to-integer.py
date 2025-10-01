class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        curr = values.get(s[-1])
        for i in reversed(range(len(s)-1)):
            if values.get(s[i]) < values.get(s[i+1]):
                curr -= values.get(s[i])
            else:
                curr += values.get(s[i])  
        return curr     