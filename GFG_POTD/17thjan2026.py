#Expression contains redundant bracket or not
class Solution():
    def checkRedundancy(self, s):
        stack = []
        ops = set(['+', '-', '*', '/'])
        
        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                has_operator = False
                
                # pop until '('
                while stack and stack[-1] != '(':
                    if stack[-1] in ops:
                        has_operator = True
                    stack.pop()
                
                # pop '('
                if stack:
                    stack.pop()
                
                # if no operator found, it's redundant
                if not has_operator:
                    return True
        
        return False
