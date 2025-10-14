

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        count = 0
        vowels = "aeiou"

        # Initialize first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count  

        # Slide the window
        for i in range(k, len(s)):
            if s[i - k] in vowels:  
                count -= 1
            if s[i] in vowels:      
                count += 1
            max_count = max(max_count, count)

        return max_count
