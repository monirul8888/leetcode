class Solution(object):
    def maxArea(self, height):

        start=0
        end=len(height)-1
        total=0

        while(end>start):
            h=min(height[start],height[end])
            w=end-start
            total=max(total,h*w)

            if(height[end]>height[start]):
                start+=1
            else:
                end-=1
        return total
