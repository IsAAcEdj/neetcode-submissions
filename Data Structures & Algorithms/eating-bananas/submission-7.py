class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bound = max(piles)
        bounds = []
        k = bound
        l = 1
        r = max(piles)
        while(l <= r):
            time = 0
            mid = (l + r) // 2
            for j in piles:
                time += math.ceil(j / mid)
            if(time > h):
                l = mid + 1
            else:
                r = mid - 1
                if(mid < k):
                    k = mid
        return k