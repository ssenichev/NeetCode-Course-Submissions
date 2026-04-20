class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # from collections import defaultdict
        # ids = defaultdict(lambda: 0)
        ids = {}

        for i, n in enumerate(nums):
            needed = target - n
            if needed in ids:
                return [ids.get(needed), i]
            else:
                ids[n] = i