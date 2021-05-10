# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# Rotate the array A by K times
#   e.g. 
#       A = [3, 8, 9, 7, 6]
#       K = 3
#   process:
#       1). [3, 8, 9, 7, 6] 
#       2). [6, 3, 8, 9, 7] 
#       3). [7, 6, 3, 8, 9]
#       4). [9, 7, 6, 3, 8]
#
# <Solution>
#   - 先找到頭元素 (透過K, len(A))
#   - 將頭元素後的元素依序加到新陣列中, 最後再將頭元素前的元素加到新陣列中(暫存於Buffer)

# <其他限制>
#   - N(length of A)和K為介於0~100的整數
#   - 陣列中的整數介於-1000~1000之間

def solution(A, K):
    # write your code in Python 3.6
    rotated_array = rotate(A, K)
    return rotated_array

def rotate( array:list, rotation_times:int) -> list:
    """ Return a rotated list """
    array_length = len(array)
    rotation_times %= array_length

    if rotation_times==0:
        return array

    if rotation_times == 1:
        head = [array[array_length-1]]
    else:
        head = array[(rotation_times-1):]
        
    tail = array[:(array_length-rotation_times)]

    rotated_array = head + tail

    return rotated_array
