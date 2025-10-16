class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        old=sum(nums[:k])
        new=old
        for i in range(k,len(nums)):
            old=old+nums[i]-nums[i-k]
            new=max(new,old)
        return new/k