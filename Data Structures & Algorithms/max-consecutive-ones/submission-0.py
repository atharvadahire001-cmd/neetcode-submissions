class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        soln=[]
        for i in nums:
            if i==1:
                count+=1
            if i!=1:
                soln.append(count)
                count=0
        soln.append(count)
        return max(soln)