class Solution(object):
    def largestAltitude(self, gain):
        gain.insert(0,0)
        count=0
        for i in range(1,len(gain)):
            gain[i]=gain[i]+gain[i-1]
            count=max(gain[i],count)
        return count

        