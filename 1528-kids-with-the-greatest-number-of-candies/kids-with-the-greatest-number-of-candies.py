class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
       
       result=[]
       for i in range(len(candies)):
        c=extraCandies+candies[i]
        max_c=max(candies)
        if(c>=max_c):
            result.append(True)
        else:
            result.append(False)
       return result



        