class Solution(object):
    def findDifference(self, nums1, nums2):
        
        s1=set(nums1)
        s2=set(nums2)
        l1=list(s1-s2)
        l2=list(s2-s1)

        return [l1,l2]