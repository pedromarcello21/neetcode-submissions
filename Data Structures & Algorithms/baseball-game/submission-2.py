class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in operations:
            if i == "C":
                result.pop()
            elif i == "D":
                result.append(result[-1] * 2)
            elif i == "+":
                result.append(int(result[-1]) + int(result[-2]))
            else:
                result.append(int(i))
        return sum(result)
                
        