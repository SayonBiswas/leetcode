class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for paren in s:
            if paren in '({[':
                stack.append(paren)
            elif paren in ')}]':
                if not stack or stack[-1] != pairs[paren]:
                    return False
                stack.pop()
        return len(stack) == 0