class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
                continue
            val2 = stack.pop()
            val1 = stack.pop()

            if token == "+":
                result = val1 + val2
            elif token == "-":
                result = val1 - val2
            elif token == "*":
                result = val1 * val2
            elif token == "/":
                result = int(val1 / val2)
            stack.append(result)
        return stack.pop()
            
            
              