class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        res = 0
        right = 0
        v = set()
        while right < len(s):
            if s[right] in v:
                res = max(res, right-left)
                while(s[left] != s[right]):
                    v.remove(s[left])
                    left += 1
                v.remove(s[left])
                left += 1
            else:
                v.add(s[right])
                right += 1
        res = max(res, right-left)
        return res
