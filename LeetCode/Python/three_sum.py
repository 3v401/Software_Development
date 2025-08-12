# URL: https://leetcode.com/problems/3sum/description/

def threesum(nums: list[int]) -> list[list[int]]:

    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i]==nums[i-1]:
            # if i > 0 and is duplicate, jump to the next non duplicate i
            continue

        # order of pointers in sum [i, lpoint, rpoint]
        lpoint = i + 1
        rpoint = len(nums)-1
        while lpoint < rpoint:

            totalsum = nums[i] + nums[lpoint] + nums[rpoint]

            if totalsum < 0:
                # totalsum is too low, higher numbers required -> increase lpoint
                lpoint += 1
            elif totalsum > 0:
                # totalsum is too high, lower numbers required -> decrease rpoint
                rpoint -= 1
            else:
                result.append([nums[i], nums[lpoint], nums[rpoint]])
            
                while lpoint < rpoint and nums[lpoint]==nums[lpoint+1]:
                    # if after finding the solution, the next lpoint is duplicate
                    lpoint += 1
                while lpoint < rpoint and nums[rpoint] == nums[rpoint-1]:
                    # if after finding the solution, the next (i-1) rpoint is duplicate
                    rpoint -= 1
                
                # if there are no duplicates in lpoint, rpoint:
                lpoint += 1
                rpoint -= 1

    return result

if __name__ == "__main__":
    print(threesum([-1,0,1,2,-1,-4]))
    print(threesum([0,1,1]))
    print(threesum([0,0,0]))