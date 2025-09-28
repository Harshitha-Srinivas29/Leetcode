class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Add "(" if open < n
        # Add ")" if close < open
        # Stop if open == close == n
        stack = []
        result = []
        def backtrack(openP, close):
            if openP == close == n:
                result.append("".join(stack))
                return
            if openP < n:
                stack.append("(")
                backtrack(openP +1, close)
                stack.pop()
            if close < openP:
                stack.append(")")
                backtrack(openP, close+1)
                stack.pop()
        backtrack(0,0)
        return result
            