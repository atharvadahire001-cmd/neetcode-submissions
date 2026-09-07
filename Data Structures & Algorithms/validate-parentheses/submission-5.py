class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brac_matches={')':'(',']':'[','}':'{'}
        for i in s:
            if i in brac_matches:
                if stack and stack[-1]==brac_matches[i]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False