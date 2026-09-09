class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        cur = 0
        for num in numSet:
            if num-1 not in numSet:
                cur = 1
        
                while num + cur in numSet:
                    cur += 1
                
                res = max(res,cur)
    
        return res