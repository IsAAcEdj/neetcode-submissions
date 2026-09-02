class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        t = 0
        retur = []
        for i, n in enumerate(nums):
            if target - n in nums[:i] or target - n in nums[i + 1:]:
                 retur.append(i)
        return retur
                 