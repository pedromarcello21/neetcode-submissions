#Round 2
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_consecutive = 0
        for i in nums:
            if i == 1:
                count +=1
                if count > max_consecutive:
                    max_consecutive = count
            if i == 0:
                count = 0
        return max_consecutive