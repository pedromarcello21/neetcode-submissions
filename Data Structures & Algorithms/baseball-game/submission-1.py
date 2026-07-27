class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for i in operations:
            if i not in ["C", "D", "+"]:
                records.append(int(i))
            elif i == "C":
                records.pop()
            elif i == "D":
                records.append(records[-1] * 2)
            elif i == "+":
                records.append(records[-1] + records[-2])
        return sum(records)

                
        