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

        for a in range(len(s1)):
            window[s2[a]] = window.get(s2[a], 0) + 1

        while right < len(s2):
            if window == h:
                return True

            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1
            right += 1

            if right < len(s2):
                window[s2[right]] = window.get(s2[right], 0) + 1
        return False