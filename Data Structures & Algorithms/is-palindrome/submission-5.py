class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while (l <= r):
            if (not s[l].isalnum()):
                l += 1
                if l > r:
                    return True
                continue
            if (not s[r].isalnum()):
                print('f')
                r -= 1
                if l > r:
                    return True
                continue
            if (s[l] != s[r]):
                return False
            l += 1
            r -= 1
        return True