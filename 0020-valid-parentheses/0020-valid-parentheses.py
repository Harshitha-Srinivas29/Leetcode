class Solution:
    def isValid(self, s: str) -> bool:
        match = {')' : '(', '}' : '{', ']' : '['}
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c in '[({':
                stack.append(c)
            else:
                if not stack or stack[-1] != match.get(c, None):
                    return False
                stack.pop()
        return True
        