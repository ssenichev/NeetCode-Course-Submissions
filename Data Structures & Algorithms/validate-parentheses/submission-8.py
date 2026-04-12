class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ')': '(',
            '}': '{',
            ']': '['
            }

        for br in s:
            if br in ['(', '{', '[']:
                stack.append(br)
            elif len(stack) > 0:
                op = stack.pop()
                if match.get(br) != op:
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False