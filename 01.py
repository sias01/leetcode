class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3 2 4
        # target = 6
        for i in range (0, len(nums)):
            print(nums[i])
            for j in range(i+1, len(nums)):
                
                #print(nums[j])
                if(nums[i] + nums[j]==target):
                    return [i,j]
        return None