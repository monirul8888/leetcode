class Solution(object):
    def gcdOfStrings(self, str1, str2):
        
        if((str1+str2)!=(str2+str1)):
            return ""
        else:
            n1=len(str1)
            n2=len(str2)
            
            while(n2!=0):
                r=n1%n2
                n1=n2
                n2=r
            return(str1[:n1])

        