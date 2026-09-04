class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)- 1):
            current_max = max(arr[i+1:])
            arr[i] = current_max
        arr[-1] = -1
        return arr
            