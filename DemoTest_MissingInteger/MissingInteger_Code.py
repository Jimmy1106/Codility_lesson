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




    
        

