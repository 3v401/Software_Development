# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/description/

"""
For this problem we will do a modified binary search with O(log(min(n,m))) runtime

NOTE: STUDY THIS EXERCISE AGAIN
"""

class Solution:

    def motsa(self, nums1: list[int], nums2: list[int])-> int:

        if len(nums1) > len(nums2):
            # sort the lists. The shortest list goes first (to optimize runtime)
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m+n+1)//2
        # number of elements on the left side of the merged list

        lo_cut, hi_cut = 0, m
        # lowest possible cut position in nums1
        # highest possible cut position in nums1
        # search bounds for the binary search in index i of the shortest array (nums1)

        while lo_cut <= hi_cut:

            i = (lo_cut + hi_cut)//2
            # cut position in nums1
            j = total_left -i
            # cut position in nums2

            # edge values to iterate inside list:
            # nums1: left (smallest) and right (biggest)
            L1 = nums1[i-1] if i>0 else float('-inf')
            R1 = nums1[i] if i<m else float('inf')
            # nums2: left (smallest) and right (biggest)
            L2 = nums2[j-1] if j>0 else float('-inf')
            R2 = nums2[j] if j<n else float('inf')

            if L1<=R2 and L2<=R1:
                # found correct partition
                if (m+n)%2==1:
                    # if it is odd, the median:
                    return float(max(L1, L2))
                # if it is even, the median:
                return (max(L1, L2) + min(R1, R2)) /2.0
            
            elif L1>R2:
                # The cut in the smaller array nums1 is too far to the right -> move to the left
                hi_cut = i-1
            elif L2 > R1:
                # The cut in the smaller array nums1 is too far to the left -> move to the right
                lo_cut = i+1

        # If after all these steps no solution is found, there is an error in the input
        raise ValueError("Arrays not sorted or invalid input")

if __name__ == "__main__":
    sol = Solution()
    print(sol.motsa([1, 3], [2]))
    print(sol.motsa([1,2,3,4,5,6,7,8], [3, 4]))
    print(sol.motsa([1,2,3,4,5,6,7,100,101,102], [8,9,10,11,12,13,14,15,16,17]))    # Good example: Makes moves right and left several times (4 iterations in total)
    print(sol.motsa([5,6,7,8], [1,2]))
    print(sol.motsa([2], []))