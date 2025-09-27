class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False #odd length
        match = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for c in s:
            if c in '[({':
                stack.append(c)
            else:
                if not stack or stack[-1] != match.get(c, None):
                    return False
                stack.pop()
        return not stack
        # stack must be empty after returning all the elements
        