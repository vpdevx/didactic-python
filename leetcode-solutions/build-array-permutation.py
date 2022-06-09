class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        fin = []
        
        for i in range(len(nums)):
            fin.append(nums[nums[i]])
        return fin
if __name__ == '__main__':
    nums =  []
    nums.random.randint(1 , size = 6)p
    build(nums)
