class Solution(object):
    def maxArea(self, height):

        old=0
        lp=0
        rp=len(height)-1
        while(rp>lp):
            w=rp-lp
            h=min(height[rp],height[lp])
            old=max(old,(w*h))

            if(height[rp]>height[lp]):
                lp+=1
            else:
                rp-=1
        return old

       
        