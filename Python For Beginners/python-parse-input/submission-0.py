from typing import List

def read_integers() -> List[int]:
    a=input()
    L=a.split(",")
    for i in range(len(L)):
        L[i]=int(L[i])
    return L



# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
