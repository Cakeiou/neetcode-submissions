class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ('(', '{', '[')
        for i in s:
            if i in open:
                stack.append(i)
                continue
            
            if len(stack) == 0:
                return False

            match i:
                case ')':
                    if stack.pop() != '(':
                        return False
                case '}':
                    if stack.pop() != '{':
                        return False
                case ']':
                    if stack.pop() != '[':
                        return False
                case _:
                    return False
        if len(stack) == 0:
            return True
        return False
                
