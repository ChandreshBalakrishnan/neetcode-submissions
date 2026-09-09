class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = 1
        c = 0
        for num in nums:
            if num == 0:
                c += 1
            else:
                m = num*m
        if c > 1:
            output = [0 for _ in range(len(nums))]
            return output
        output = [m for _ in range(len(nums))]
        for i in range(len(output)):
            if (c == 1):
                if(nums[i] == 0):
                    output[i] = m
                else:
                    output[i] = 0
            else:
                output[i] = output[i]//nums[i]
            
        return output