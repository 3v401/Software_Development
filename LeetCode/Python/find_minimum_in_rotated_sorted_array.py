# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def fmirsa(nums: list[int]) -> int:
    
    left, right = 0, len(nums)-1
    while left < right:
        
        mid = (left + right)//2
        if nums[mid] < nums[right]:
            # minimum is at the left
            right = mid
        else:
            # minimum is at the right
            left = mid +1
    
    return nums[left]