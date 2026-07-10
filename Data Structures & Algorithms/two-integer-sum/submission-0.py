class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        first get a number
        find the needed num = target - nums
        check if the target exists already in a hashStore:
            if it exists return the index for this index should be the val
        if not make a map like
            hashMap[num] = index

        '''

        hashMap = {}
        for i in range(len(nums)):
            neededNum = target - nums[i]

            if neededNum in hashMap and hashMap[neededNum] != i:
                return sorted([i, hashMap[neededNum]])
            
            else:
                hashMap[nums[i]] = i
        
        return []
