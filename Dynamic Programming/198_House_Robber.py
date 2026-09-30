class Solution:
    def rob(self, nums: list[int]) -> int:
        next1 = 0
        next2 = 0
        for i in range( len(nums)-1, -1, -1):
            curr = max(nums[i] + next2, next1)
            next2 = next1
            next1 = curr
        return next1

solution = Solution()
result = solution.rob([2,7,9,3,1])
print(result)