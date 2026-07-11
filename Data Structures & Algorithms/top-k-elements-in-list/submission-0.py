class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        ans = []

        for n in nums:
            countMap[n] += 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in countMap.items():
            bucket[freq].append(num)

        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans
        
        
