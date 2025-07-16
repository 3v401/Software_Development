# Optimized
# URL: https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

def movezeros(nums: list[int]) -> list[int]:
  
  insert_pos = 0

  for num in nums:
    if num != 0:
      nums[insert_pos] = num
      insert_pos += 1

  for i in range(insert_pos, len(nums)):
    nums[i]=0
  
  return nums

"""
# Not optimal:
def movezeros(nums: list[int]) -> list[int]:
  
  for i in range(len(nums)):
    if nums[i] == 0:
      nums.pop(i)
      nums.append(0)
    else:
      continue
  return nums
"""

if __name__ == "__main__":
  print(movezeros([0,1,0,3,12]))
  print(movezeros([0]))