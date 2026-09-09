class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            target = -num
            left = i + 1
            right = len(nums)-1

            while(left < right):
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while(left < right and nums[left] == nums[left-1]):
                        left += 1

        return res