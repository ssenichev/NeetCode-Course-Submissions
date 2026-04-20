class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ids = {}

        for i, n in enumerate(nums):
            needed = target - n
            if target - n in ids:
                return [ids.get(needed), i]
            else:
                ids[n] = i