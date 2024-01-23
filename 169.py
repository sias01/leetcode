class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in nums:
            if i in count:
                count[i] += 1
                if count[i]>n/2:
                    print(i)
                    return i
            else:
                count[i] = 1
        return None
        