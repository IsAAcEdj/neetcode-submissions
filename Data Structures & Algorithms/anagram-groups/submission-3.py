class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = []
        dict = defaultdict(list)
        for i in strs:
            cur = "".join(sorted(i))
            dict[cur].append(i)
        for i in dict:
            r.append(dict[i])
        return r