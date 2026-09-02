class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max = 1
        if len(s) == 0: return 0
        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                cur = 0
                j = 0
                while nums[i] + j in s:
                    cur += 1
                    j += 1
                if cur > max: max = cur
        return max
