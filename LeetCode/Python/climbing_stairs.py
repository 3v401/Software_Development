# URL: https://leetcode.com/problems/climbing-stairs/description/

"""
Not optimal version:

Runtime O(n)
Access memory O(n)

def climbing_stairs(n: int) -> int:

    if n <=2:
        # edge case, n<=2 are n steps
        return n
    
    dp = [0]*(n+1)
    # [0]*n gives indexes [0,n-1]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    # n is the input (last number)
    return dp[-1]
"""

"""
Optimal version:

Runtime O(n)
Space O(1)
"""

def climbing_stairs(n: int) -> int:

    if n <= 2:
        return n
    
    first = 1
    second = 2

    for i in range(3, n+1):

        result = first + second
        first = second
        second = result

    return result

if __name__ == "__main__":

    print(climbing_stairs(2))
    print(climbing_stairs(3))
    print(climbing_stairs(5))