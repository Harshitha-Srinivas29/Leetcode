class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        digi_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqra",
            "8" : "tuv",
            "9" : "wxyz"
        }

        
        def backtrack(combination, next_digi):
            if len(next_digi) == 0:
                output.append(combination)
            else:
                for letter in digi_map[next_digi[0]]:
                    backtrack(combination + letter, next_digi[1:])
        output = []
        backtrack("", digits)
        return output