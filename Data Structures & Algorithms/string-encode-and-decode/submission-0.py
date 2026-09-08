class Solution:

    def encode(self, strs: List[str]) -> str:
        l = ""
        for i in strs:
            l += (i + "~")
        return l
    def decode(self, s: str) -> List[str]:
        return s.split("~")[:-1]
        