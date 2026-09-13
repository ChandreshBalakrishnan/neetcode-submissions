class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        openH = {'(': ')', '[': ']', '{': '}', 0: 0}
        for b in s:
            if b in openH:
                stack.append(b)
            elif b in openH.values():
                if openH[stack[-1]] == b:
                    stack.pop()
                else:
                    return False
        if stack == [0]:
            return True
        return False