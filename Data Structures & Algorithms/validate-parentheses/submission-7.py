class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openH = {'(': ')', '[': ']', '{': '}'}
        for b in s:
            if b in openH.keys():
                stack.append(b)
            elif not stack or openH[stack[-1]] != b:
                return False
            else:
                stack.pop()
        return not stack