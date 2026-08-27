class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max = (r - l) * min(heights[l], heights[r])
        while l <= r:
            cur = (r - l) * min(heights[l], heights[r])
            if(cur > max):
                max = cur
            if(heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
        return max

        