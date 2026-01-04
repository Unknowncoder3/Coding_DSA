#parenthesis checking in a string
def are_parentheses_balanced(s):
    stack = []
    opening = set('({[')
    closing = set(')}]')
    matches = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()

    return len(stack) == 0
# Example usage:
s = input("Enter a string with parentheses: ")
if are_parentheses_balanced(s):
    print("Parentheses are balanced")
else:
    print("Parentheses are not balanced")
    