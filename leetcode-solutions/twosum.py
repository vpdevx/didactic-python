class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [3, 7, 8, 9]
        target = 15
        seen = {}
        for i, b in enumerate(nums):
            a = target - b
            print("b = ", b)
            print(i)
            if a in seen:
                print(i)
                return [seen[a], i]
            seen[b] = i