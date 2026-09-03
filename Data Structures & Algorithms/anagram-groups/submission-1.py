class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = []
        dict = {}
        for i in strs:
            cur = "".join(sorted(i))
            if cur not in dict:
                dict[cur] = []
            dict[cur].append(i)
        for i in dict:
            r.append(dict[i])
        return r