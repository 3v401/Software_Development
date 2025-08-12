# URL: https://leetcode.com/problems/longest-consecutive-sequence/description/

def lcs(nums: list[int]) -> int:

  numset = set(nums)
  maxlen = 0

  for num in numset:

    if num-1 not in numset:
      # find the first element of sequence
      length = 1
      while num + length in numset:
        # find the last consecutive element of sequence
        length +=1
      
      maxlen = max(maxlen, length)
      # longest consecutive substring length
  return maxlen


if __name__ == "__main__":
  print(lcs([100,4,200,1,3,2]))
  print(lcs([0,3,7,2,5,8,4,6,0,1]))
  print(lcs([1,0,1,2]))