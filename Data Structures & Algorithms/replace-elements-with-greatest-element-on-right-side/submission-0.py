class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        for i in range(len(arr) -1, -1, -1):
            temp = arr[i]  # Save the current element before we overwrite it
            arr[i] = current_max  # Replace current element with the max from its right
            if temp > current_max:  # Check if current element is larger than what we've tracked
                current_max = temp  # Update the max for the next iteration (going leftward)
        return arr