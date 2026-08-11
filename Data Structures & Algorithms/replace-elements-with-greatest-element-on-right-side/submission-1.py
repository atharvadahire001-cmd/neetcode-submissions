class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        dup=[]
        for i in range(len(arr)-1):
            dup=arr[i+1:]
            arr[i]=max(dup)
        arr[len(arr)-1]=-1
        return arr
