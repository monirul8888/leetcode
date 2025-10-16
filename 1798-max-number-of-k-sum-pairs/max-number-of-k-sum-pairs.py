class Solution(object):
    def maxOperations(self, nums, k):
        count=0
        nums.sort()

        start=0
        end=len(nums)-1
        while(end>start):
            sum=nums[start]+nums[end]
            if (k>sum):
                start+=1
            elif (sum>k):
                end-=1
            else:
                count+=1
                end-=1
                start+=1
        return count
        