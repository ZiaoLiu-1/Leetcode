
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        # A function to compute the sign of a number
        def sign(x: int) -> int:
            return (x > 0) - (x < 0)

        prev_diff = nums[1] - nums[0]
        count = 1 if prev_diff == 0 else 2
        
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if sign(diff) != sign(prev_diff) and diff != 0:
                count += 1
                prev_diff = diff

        return count


