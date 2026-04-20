class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        
        d = defaultdict(lambda: 0)
        freq = [[] for _ in range(len(nums) + 1)]
        answer = []

        for num in nums:
            d[num] += 1

        for val, count in d.items():
            freq[count].append(val)

        for i in range(len(freq)-1, -1, -1):
            answer.extend(freq.pop(i))
            
            if len(answer) == k:
                return answer

        return []

        
