class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * len(nums)
        
        left = 1
        for i in range (n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range (n-1, -1, -1):
            answer [i] *= right
            right *= nums[i]

        return answer

solution = Solution()
result = solution.productExceptSelf([1, 2, 3, 4])
print(result)