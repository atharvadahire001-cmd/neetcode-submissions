class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dup=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]='_'
                count+=1
            else:
                dup.append(nums[i])
        for i in range(len(dup)):
            nums[i]=dup[i]
        for j in range(len(nums)-1,len(dup)-1,-1):
            nums[j]='_'
        k=int(len(nums)-count)
        return k       