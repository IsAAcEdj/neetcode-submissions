class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for i in strs:
            cur = "".join(sorted(i))
            dict[cur].append(i)
        return list(dict.values())