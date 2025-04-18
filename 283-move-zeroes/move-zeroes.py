class Solution(object):
    def moveZeroes(self, nums):
        nonZero=[]
        zero=[]
        for num in nums:
            if num==0:
                zero.append(num)
            else:
                nonZero.append(num)
        result=nonZero+zero
        for i in range(len(result)):
            nums[i]=result[i]
        
