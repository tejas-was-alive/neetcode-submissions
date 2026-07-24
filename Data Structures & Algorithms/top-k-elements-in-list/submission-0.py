class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        counts = [[] for _ in range(n + 1)]
        for key, val in count.items():
            counts[val].append(key)
        res = []
        for i in range(n, -1, -1):
            if k == 0:
                break
            
            while counts[i] and k > 0:
                key = counts[i].pop()
                res.append(key)
                k -= 1
        return res