class Solution(object):
    def removeDuplicates(self, nums):
        unique=[]
        
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                continue
            else:
                unique.append(nums[i])
        unique.append(nums[-1])

        for i in range(len(unique)):
            nums[i]=unique[i]
        return len(unique)




        