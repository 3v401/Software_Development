# URL: https://leetcode.com/problems/basic-calculator/description/

class Solution:
    def calculator(self, s: str) -> int:
        num = 0
        res = 0
        sign = 1
        stack = []
        for char in s:
            if char.isdigit():
                num = num*10+int(char)
                # build >1 digits number if needed (i.e., 10, 200, 3000...)
            elif char == '+':

                res += sign*num
                num = 0
                sign = 1

            elif char == '-':

                res += sign*num
                num = 0
                sign = -1

            elif char == '(':

                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            elif char == ')':

                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0

            # everything else (like ' '), ignore

        res += sign*num
        return res
    
if __name__ == '__main__':

    sol = Solution()
    print(sol.calculator("(1+(4+5+2)-3)+(6+8)"))
    print(sol.calculator(" 2-1 + 2 "))