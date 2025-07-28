# URL: https://leetcode.com/problems/single-number-iii/description/

"""
NOT correct solution: Counter has Space complexity O(n) and they ask for O(1)

from collections import Counter

def singlenumber(nums: list[int]) -> list[int]:

  freqnum = Counter(nums)

  solution = []
  for element in freqnum:
    if freqnum[element]==1:
      solution.append(element)

  return solution
"""

def singlenumber(nums: list[int]) -> list[int]:

  xor_total = 0
  for num in nums:
    # a^a = 0, we want to get the non-repeated
    xor_total ^= num

  bit_diff = xor_total & -xor_total
  # 6&-6 gives back the bit difference of the set
  x = 0
  y = 0
  # two variables because there are two different number always (3 if 3)
  for num in nums:
    if bit_diff & num:
      # If belongs to group 1
      x ^=num
      # The repeated terms will end up being 0
    else:
      # If belongs to group 2
      y ^= num
      # The repeated terms will end up being 0

  return [x,y]

if __name__ == "__main__":
  
  print(singlenumber([1,2,1,3,2,5]))
  print(singlenumber([-1,0]))
  print(singlenumber([0,1]))