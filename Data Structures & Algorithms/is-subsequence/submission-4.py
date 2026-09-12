class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = 0
        for i in s:
            print(i)
            print(pos)
            print(t[pos:].find(i))
            if t[pos:].find(i) > -1:
                pos = pos + t[pos:].find(i) + 1
            else:
                return False
        return True