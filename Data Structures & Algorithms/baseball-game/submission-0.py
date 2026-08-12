class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for i in range(len(operations)):
            if operations[i]=='+':
                record.append(int(record[len(record)-1]+record[len(record)-2]))
            elif operations[i]=='D':
                t=2*record[len(record)-1]
                record.append(t) 
            elif operations[i]=='C':
                temp=[]
                j=0
                while j<len(record)-1:
                    temp.append(record[j])
                    j+=1
                record=temp
            else:
                record.append(int(operations[i]))
        return sum(record)

