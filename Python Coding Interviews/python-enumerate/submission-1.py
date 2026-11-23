from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    ans=-1
    for i,num in enumerate(nums):
        if num==7:
            ans= i
            break
    return ans 
    


def get_dist_between_sevens(nums: List[int]) -> int:
    num_seven=[]
    for i,num in enumerate(nums):
        if num==7 and len(num_seven)<2:
            num_seven.append(i)
    return num_seven[1]-num_seven[0]



# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
