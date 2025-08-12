# URL: https://leetcode.com/problems/maximum-product-subarray/description/

def mps(nums: list[int]) -> int:

    if not nums:
        # if nums is empty
        return 0
    
    maxproduct_final = nums[0]
    #maximum product subarray
    maxproduct = nums[0]
    #maximum product each iteration
    minproduct = nums[0]
    # minimum product each iteration (required for negative products)

    for num in nums[1:]:

        if num < 0:
            # if negative, we must invert to maximize and minimize the real final products
            maxproduct, minproduct = minproduct, maxproduct

        maxproduct = max(num, maxproduct*num)
        minproduct = min(num, minproduct*num)

        maxproduct_final = max(maxproduct_final, maxproduct)

    return maxproduct_final

if __name__ == "__main__":

    print(mps([2,3,-2,4]))
    print(mps([-2,0,-1]))