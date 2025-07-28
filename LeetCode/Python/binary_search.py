# https://leetcode.com/problems/binary-search/description/

"""
1. Create two pointers: left and right. Compute mid term
2. If nums[mid] == target --> target found
3. if nums[mid] < target --> move to the right
4. if nums[mid] > target --> move to the left
5. After all the numbers, if not found --> return -1
"""

def binarysearch(nums: list[int], target: int) -> int:

    left, right = 0, len(nums)-1
    # len(nums) -1 to not exceed index (0, ..., n-1)
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            # target found, return index
            return mid
        elif nums[mid] < target:
            # target is in the right
            left = mid +1
        else:
            # target is in the left
            right = mid - 1
    # if number not found return -1
    return -1

if __name__ == "__main__":
  print(binarysearch([-1,0,3,5,9,12], 9))
  print(binarysearch([-1,0,3,5,9,12], 2))