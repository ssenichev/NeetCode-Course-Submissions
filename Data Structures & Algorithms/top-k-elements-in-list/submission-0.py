class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
        return [k for k,v in d][:k]