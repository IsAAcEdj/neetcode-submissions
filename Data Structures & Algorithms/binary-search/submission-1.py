class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums)
        if target not in nums:
            return -1
        while(beg < end):
            mid = int((beg + end) / 2)
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                end = mid
            else:
                beg = mid