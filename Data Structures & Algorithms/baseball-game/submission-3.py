class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for i in range(len(operations)):
            if operations[i]=="+":
                ans.append(int(ans[-1]+ans[-2]))
            elif operations[i]=="D":
                ans.append(int(2*ans[-1]))
            elif operations[i]=="C":
                ans.pop()
            else:
                ans.append(int(operations[i]))
        return sum(ans)