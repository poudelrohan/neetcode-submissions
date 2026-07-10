class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()
        for n in nums:
            if n in seenNums:
                return True
            else:
                seenNums.add(n)
        return False