class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []
        val = 0

        for token in tokens:
            if token == "+":
                val = stack.pop(-2) + stack.pop(-1)
                stack.append(val)
            elif token == "-":
                val = stack.pop(-2) - stack.pop(-1)
                stack.append(val)
            elif token == "*":
                val = stack.pop(-2) * stack.pop(-1)
                stack.append(val)
            elif token == "/":
                val = int(stack.pop(-2) / stack.pop(-1))
                stack.append(val)
            else:
                stack.append(int(token))

        return val