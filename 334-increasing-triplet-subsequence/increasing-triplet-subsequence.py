class Solution(object):
    def increasingTriplet(self, nums):
        small = float('inf')
        mid = float('inf')

        for x in nums:
            if x <= small:
                small = x        
            elif x <= mid:
                mid = x            
            else:
                return True        

        return False
