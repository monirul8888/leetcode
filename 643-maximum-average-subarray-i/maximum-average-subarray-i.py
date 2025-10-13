class Solution(object):
    def findMaxAverage(self, nums, k):
        # sum of first k elements
        total = sum(nums[:k])
        old = total

        
        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]  
            if total > old:
                old = total

        return float(old) / k
