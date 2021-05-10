# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# <釐清問題>
#   - 找到最小的正整數, 且該正整數未出現於陣列中
#   e.g.
#   A = [1, 3, 6, 4, 1, 2], the function should return 5.

# <其它限制>
# Given A = [1, 2, 3], the function should return 4.
# Given A = [-1, -3], the function should return 1.
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [-1,000,000..1,000,000].

def solution(A):
    return findMinDisappearInteger(A)


def findMinDisappearInteger(array) -> int:
    non_duplicated_array = list(set(array))
    
    sorted_array = sorted(non_duplicated_array)

    cnt = 1
    for element in sorted_array:
        if element < 1:
            continue
        else:
            if cnt == element:
                cnt += 1
            else:
                break
    return cnt

def findMinDisappearInteger2(array) -> int:

    table = set()
    
    cnt = 1
    for element in array:
        if element < 1:
            continue
        table.add(element)
        while cnt in table:
            cnt += 1
    return cnt

def findMinDisappearInteger3(array) -> int:

    table = {}
    non_duplicated_array = set(array)
    nd_array_length = len(non_duplicated_array)
    for integer in range(1,nd_array_length+1):
        table[integer] = False
 
    for integer in non_duplicated_array:
        table[integer] = True
    
    for key,value in table.items():
        if value == False:
            return key
    return nd_array_length+1

def findMinDisappearInteger4(array) -> int:

    table = {}
    array_length = len(array)
    for integer in range(1,array_length+1):
        table[integer] = False
 
    for integer in array:
        table[integer] = True
    
    for key,value in table.items():
        if value == False:
            return key
    return array_length+1

import timeit
# A = [1, 3, 6, 4, 1, 2]
A = list(range(100000+1))
# A.remove(999)
# print(findMinDisappearInteger(A))
print(timeit.timeit("findMinDisappearInteger(A)", setup="from __main__ import findMinDisappearInteger,A", number=1))

for i in [2,3,4]:
    print(timeit.timeit("findMinDisappearInteger%d(A)"%i, setup="from __main__ import findMinDisappearInteger%d,A"%i,number=1))


    