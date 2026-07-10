class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        take on s from strs:
            convert it into list, then sort it, then combine again to str
            check if that sorted Str is a hashkey:
                if yes then store the original string in the val of that key
                if NO then make it a hashMapkey and sotre its unsorted stirng as value
                at the end print all the values of the hashmaps
        '''
        hashMap = defaultdict(List)
        ans = []

        for s in strs:
            sList = list(s)
            sList.sort()
            sortedWord = "".join(sList)
            if sortedWord in hashMap:
                hashMap[sortedWord].append(s)
            else:
                hashMap[sortedWord] = [s]
        
        for value in hashMap.values():
            ans.append(value)
        
        return ans

