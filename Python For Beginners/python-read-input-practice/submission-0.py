def add_two_numbers() -> int:
    a=input()
    L=a.split(",")
    for i in range(len(L)):
        L[i]=int(L[i])
    return sum(L)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
