from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # strs = [] returns ""
        if len(strs) == 0:
            return ""

        encodedArr = []
        for s in strs:
            tempLen = len(s)
            delimiter = str(tempLen) + "*"
            encodedArr.append(delimiter)
            encodedArr.append(s)
        
        return "".join(encodedArr)


    def decode(self, s: str) -> List[str]:
        # Encode returns "" for an empty list, so we must return []
        if s == "":
            return []
        
        decodedArr = []
        i = 0
        
        # We must use a while loop so we can manually control 'i'
        while i < len(s):
            tempNum = 0
            
            # 1. Parse digits until we hit the '*' delimiter
            while s[i] != '*':
                tempNum = tempNum * 10 + int(s[i])
                i += 1
            
            # 2. Skip the '*' delimiter
            i += 1
            
            # 3. Extract the exact word using the length
            tempword = s[i : i + tempNum]
            decodedArr.append(tempword) # Always append, even if it's ""
            
            # 4. Jump the pointer forward by the length of the word
            i += tempNum
            
        return decodedArr