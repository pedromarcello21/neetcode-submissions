class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #define writer pointer
        write_index = 0
        #define reader pointer
        for read_index in range(len(nums)):
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                write_index += 1
        return write_index

        
        