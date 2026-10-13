class Solution:
    from collections import defaultdict
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        dict = defaultdict(int)
        res = 0
        while r >= l and r < len(s):
            if dict[s[r]] == 0:
                dict[s[r]] += 1
                r += 1
                if(r - l > res):
                    res = r - l
            else:
                dict[s[l]] -= 1
                l += 1
        return res