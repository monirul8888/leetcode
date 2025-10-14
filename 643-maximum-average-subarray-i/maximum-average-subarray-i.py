class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        old_total=sum(nums[:k])
        new_total=old_total

        for i in range(k, len(nums)):
            old_total=old_total+nums[i]-nums[i-k]

            if (old_total>new_total):
                new_total=old_total
        return float(new_total)/k
        