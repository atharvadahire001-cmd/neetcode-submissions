class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        output_arr = [-1] * len(arr)
        while i > 0:
            output_arr[i-1] = max(output_arr[i], arr[i])
            i -= 1
        return output_arr   
        
                
        
