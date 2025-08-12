# URL: https://leetcode.com/problems/unique-paths/description/

"""
Dynamic programming in 2D:

Dynamic programming is the best option. Based on the previous
number of paths we can compute the current one.

Only down/right allowed

[0][0]	[0][1]	[0][2]
[1][0]	[1][1]	[1][2]
[2][1]	[2][1]	[2][2]

1	1	1
1	2	3
1	3	6

d[1][2] = dp[0][2] + dp[1][1]
dp[2][1] = dp[1][1]+d[2][0]
dp[2][2] = dp[1][2] + d[2][1]
"""

def uniquepaths(m: int, n: int) -> int:

    if m==0 and n==0:
        # edge case
        return 0
    elif m==1 and n==1:
        # edge case
        return 1

    dp = [[1]*n for _ in range(m)]
    # create grid of n columns and m rows

    for i in range(1, m):
        for j in range(1, n):
            # we don't need to worry about boundaries i==0 with j==* and
            # i==* with j==0 since range(1,n/m)
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            # the ways to arrive to dp[i][j] are from upper row and left column

    # the goal is at [n-1][m-1]
    return dp[m-1][n-1]

if __name__ == "__main__":

    print(uniquepaths(3, 7))
    print(uniquepaths(3,2))