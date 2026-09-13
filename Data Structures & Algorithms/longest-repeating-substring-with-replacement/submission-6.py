class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        res = 0
        f = 0
        count = [0]*26

        while right < len(s):
            if f == 0:
                count[ord(s[right]) - ord('A')] += 1
            temp = sum(count) - max(count)
            if temp <= k:
                res = max(res, sum(count))
                right += 1
                f = 0
            else:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
                f = 1
        return res