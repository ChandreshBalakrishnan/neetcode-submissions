class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        v = {}
        for num in nums:
            v[num] = v.get(num, 0) + 1
        for key, value in v.items():
            buckets[value].append(key)
        res = []

        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res
