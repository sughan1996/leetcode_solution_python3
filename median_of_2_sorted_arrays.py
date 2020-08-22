class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
    
        nums1.extend(nums2)
        
        nums1 = sorted(nums1)
        
        l = len(nums1)
        
        if l%2==0:
        
            return (nums1[int(l/2)-1]+nums1[int(l/2)])/2
            
        else:
        
            return nums1[int(l/2)]
