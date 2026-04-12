class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)
        
        for i in nums:
            d[i] += 1

        d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
        return d[0][0]