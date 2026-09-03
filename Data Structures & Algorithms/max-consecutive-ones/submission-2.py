class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        max_streak = 0
        for i in nums:
            print(i)
            if i == 1:
                current_streak +=1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 0
        return max(max_streak, current_streak)

