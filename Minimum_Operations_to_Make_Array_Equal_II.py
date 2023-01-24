class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 == nums2:
                return 0
            else:
                return -1
        else:
            n= len(nums1)
            equal= 0
            u= 0
            for i in range(n):
                p= nums1[i]- nums2[i]
                if p%k != 0:
                    return -1
                    break
                u += p
                if p>0:
                    equal += p//k
            else:
                if u == 0:
                    return equal
                else:
                    return -1
