class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        t = 0
        retur = []
        dict = {}
        for i, n in enumerate(nums):
            
            if target - n in dict:
                return [dict[target - n], i]
            dict[n] = i    
        return retur
                 