# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

"""
Clues: Why binary search?
    1. You must write an algorithm O(log(n)) runtime complexity in a sorted array --> binary search
    2. The array is not fully unsorted. Just partially shifted.
    3. Search problem with index return
"""

def sirsa(nums: list[int], target: int) -> int:

    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right)//2
        if nums[mid]==target:
            # target found, return index
            return mid
        
        if nums[left] <= nums[mid]:
            # left part is ordered
            if nums[left] <= target < nums[mid]:
                # target is on left part
                right = mid -1
            else:
                # target is on the right part
                left = mid + 1
        else:
                # right part is ordered
                if nums[mid] < target <= nums[right]:
                     # target is on the right part
                     left = mid +1
                else:
                    # target is on the left part
                    right = mid -1

    return -1


if __name__ == "__main__":
  
  print(sirsa([4,5,6,7,0,1,2], 0))
  print(sirsa([4,5,6,7,0,1,2], 3))
  print(sirsa([1], 0))