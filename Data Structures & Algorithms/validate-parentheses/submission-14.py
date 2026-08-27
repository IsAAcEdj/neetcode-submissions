class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        string = s
        push = ["{", "[", "("]
        pair = {"}":"{", "]":"[", ")":"("}
        while (len(string) > 0):
            print(string[0])
            if(string[0] in push):
                stack.append(string[0])
            elif(len(stack) == 0 or pair[string[0]] != stack[-1]):
                return False
            else:
                stack = stack[:-1]
            string = string[1:]
        print(stack)
        if(len(stack) > 0):
            return False
        return True