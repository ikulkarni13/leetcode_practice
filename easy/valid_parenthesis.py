class Solution:
    def isValid_ira(self, s: str) -> bool:

        # create array open
        # create array close
        # create dict  mapping poen and close
        # create empty array stack
        # iterate thourgh the string
        # if first element in close => return false
        # if in open store in stack
        # if in close (check if stacj is empty), check if stack has the corresponding open, if yes, stack.pop(), else return false
        # at the end, if stack empty, return true else false

        #O(N)
        open_list = ['(', '{', '[']
        close_list = [')', '}', ']']

        pairs = {

            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for parenthesis in s:
            if parenthesis in close_list:
                if stack and pairs[parenthesis] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append()
        
        if not stack:
            return True
        else:
            return False
                
    # Chad's solution O(N)        
    def isValid(self, s: str) -> bool:
        matches = ['()', '[]', '{}']
        openings = ['(', '[', '{']
        stack = ['']

        for char in s:
            if (stack[-1] + char) in matches:
                stack.pop()
            elif char in openings:
                stack.append(char)
            else:
                return False
        
        return len(stack) == 1
