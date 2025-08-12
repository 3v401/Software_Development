# URL: https://leetcode.com/problems/container-with-most-water/description/


"""
The area is limited by the shorter of the two lines.
If I want a bigger area while reducing width,
I must increase the minimum height between the two lines.

If the minimum is at the left -> increase left (move left inwards)
If the minimum is at the right -> decrease rpoint (move right inwards)

If I do the opposite, area gets worse or stays the same.

We do two pointer algorithm to avoid nested loop O(n^2) and do O(n)
"""

def cwmw(height: list[int]) -> int:

    lpoint, rpoint = 0, len(height)-1
    maxarea = 0

    while lpoint < rpoint:

        width = rpoint - lpoint
        h = min(height[lpoint], height[rpoint])
        maxarea = max(maxarea, width *h)

        if height[rpoint] > height[lpoint]:
            lpoint +=1
        else:
            rpoint -= 1

    return maxarea

if __name__ == "__main__":

    print(cwmw([1,8,6,2,5,4,8,3,7]))
    print(cwmw([1,1]))