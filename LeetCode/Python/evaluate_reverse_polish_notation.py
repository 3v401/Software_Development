# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

"""
We will use stack technique to optimize runtime.
Runtime O(n)
Space O(n)
Each push/pop is O(1)
"""


class Solution:
    def erpn(self, tokens: list[str]) -> int:

        if not tokens:
            # edge case
            return None
        
        operators = {'+', '-', '/', '*'}
        stack = []
        # stack to append/pop terms (numbers)

        for token in tokens:
            # access the else first to load tokens, then operate
            if token in operators:
                # two tokens already appended in stack
                b = stack.pop()
                a = stack.pop()
                # they already are int

                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '/':
                    stack.append(int(a/b))
                    # truncate division always towards 0
                else:
                    stack.append(a*b)
                    # stack.append because this is the new 'a' term for next operation
            
            else:
                # load terms first, then operate
                stack.append(int(token))
                # token is a string -> convert to int

        # only one element must exist in stack now
        return stack.pop()
    
if __name__ == '__main__':

    sol = Solution()
    print(sol.erpn(["2","1","+","3","*"]))
    print(sol.erpn(["4","13","5","/","+"]))