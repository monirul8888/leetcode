class Solution(object):
    def reverseVowels(self, s):
       
       s = list(s)
       first=0
       last=len(s)-1

       while(last>first):
        if(s[first] not in "AEIOUaeiou"):
            first=first+1
        elif(s[last] not in "AEIOUaeiou"):
            last=last-1
        
        else:
            temp=s[first]
            s[first]=s[last]
            s[last]=temp
            last-=1
            first+=1
       return "".join(s)
