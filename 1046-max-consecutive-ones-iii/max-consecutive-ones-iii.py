class Solution(object):
    def longestOnes(self, nums, k):

        zeroCount=0
        max_ones=0
        start=0
        for end in range(len(nums)):
            if(nums[end]==0):
                zeroCount+=1
            while(zeroCount>k):
                if(nums[start]==0):
                    zeroCount-=1
                start+=1
            max_ones=max(max_ones,end-start+1)
        return max_ones
      