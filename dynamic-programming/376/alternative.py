class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        # Initialize the 2D dp array
        # 
        dp = [[1] * len(nums) for _ in range(2)]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[0][i] = dp[1][i-1] + 1
                dp[1][i] = dp[1][i-1]
            elif nums[i] < nums[i-1]:
                dp[1][i] = dp[0][i-1] + 1
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = dp[0][i-1]
                dp[1][i] = dp[1][i-1]

        return max(dp[0][-1], dp[1][-1])