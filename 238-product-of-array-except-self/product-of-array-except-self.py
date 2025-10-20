class Solution(object):
    def productExceptSelf(self, nums):
        
        n = len(nums)
        right = [1] * n  
        left  = [1] * n  
        
       
        for i in range(1, n):
            right[i] = right[i-1] * nums[i-1]  
        
    
        for i in range(n-2, -1, -1):           
            left[i] = left[i+1] * nums[i+1]     
        
        ans = []
        for i in range(n):
            ans.append(right[i] * left[i])       
        return ans
