class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        
        d = defaultdict(lambda: 0)
        freq = [[] for _ in range(len(nums) + 1)]
        answer = []

        for num in nums:
            d[num] += 1

        for val, count in d.items():
            print(val, count, freq)
            freq[count].append(val)

        print(freq)

        for i in range(len(freq)-1, -1, -1):
            answer.extend(freq.pop(i))
            print(answer)
            
            if len(answer) == k:
                return answer

        return []

        
