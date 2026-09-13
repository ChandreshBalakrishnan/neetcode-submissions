class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1)-1
        h = {}
        for s in s1:
            h[s] = h.get(s,0) + 1
        window = {}
        while right < len(s2):
            for j in range(right - left + 1):
                window[s2[j+left]] = window.get(s2[left+j], 0) + 1
            if window == h:
                return True
            
            window = {}
            left += 1
            right += 1
        return False