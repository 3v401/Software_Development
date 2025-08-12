# URL: https://leetcode.com/problems/house-robber/description/

def house_robber(nums: list[int]) -> int:

    # edge cases:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    
    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    # wether we want to steal house 1 or 0 (maximize)

    for i in range(2, len(nums)):
        # for each house
        dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        # decide whether to rob current house (nums[i]+dp[i-2]) or not (dp[i-1])

    return dp[-1]

if __name__ == "__main__":

    print(house_robber([1,2,3,1]))
    print(house_robber([2,7,9,3,1]))