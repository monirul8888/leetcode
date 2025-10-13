class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        num_z=[]
        num_nz=[]
        for i in range(len(nums)):
            if(nums[i]==0):
                num_z.append(nums[i])
                
            else:
                num_nz.append(nums[i])
        
        nums[:]=num_nz+num_z
            

        