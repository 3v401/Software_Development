# URL:
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75


# Optimal:
def gnc(candies: list[int], extraCandies: int) -> list[bool]:

  max_candies = max(candies)
  return [candies[i] + extraCandies >= max_candies for i in range(len(candies))]



"""
# Not optimal:
def gnc(candies: list, extraCandies: int) -> list:

  my_dict = {}
  for i, element in enumerate(candies):
    my_dict[i] = element
  return [my_dict[i]+ extraCandies >= max(candies) for i in range(len(candies))]
"""

if __name__ == "__main__":
  print(gnc([2,3,5,1,3], 3))
  print(gnc([4,2,1,1,2], 1))
  print(gnc([12,1,12], 10))