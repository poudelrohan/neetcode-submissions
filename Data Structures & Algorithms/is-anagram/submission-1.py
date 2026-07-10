class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countMap = {}
        for c in s:
            if c in countMap:
                countMap[c] += 1
            else:
                countMap[c] = 1
        
        for c in t:
            if c in countMap:
                countMap[c] -= 1
            
        
        for val in countMap.values():
            if val != 0:
                return False
            
        return True
