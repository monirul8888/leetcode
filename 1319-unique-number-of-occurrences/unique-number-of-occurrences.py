from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
      
        freq = Counter(arr)
        return len(set(freq.values())) == len(freq)
