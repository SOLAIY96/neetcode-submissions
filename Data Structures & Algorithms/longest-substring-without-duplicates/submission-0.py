class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = 0
        chars = set()

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            count = max(count, right - left + 1)

        return count        
                            
        