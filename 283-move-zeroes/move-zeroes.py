class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        nonZero = []
        zero = []
       

        for num in nums:
            if num ==0:
                zero.append(num)
            else:
                nonZero.append(num)
        nums[:] = nonZero + zero
