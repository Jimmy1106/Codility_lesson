# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# <釐清問題>
#   找出一奇數長度陣列的整數, 該整數在陣列中出現的次數為奇數次
# <Solution>
#   排序 -> 透過slide window倆倆比對 -> 遇到不同的元素則return window[0]

# <其他限制>
#       N is an odd integer within the range [1..1,000,000];
#       each element of array A is an integer within the range [1..1,000,000,000];
#       all but one of the values in A occur an even number of times. (只有一個整數在陣列中出現奇數次)

def solution(A):
    return findUnpairedNum(A)

def findUnpairedNum(array) -> int:
    sorted_array = sorted(array)

    sorted_array.append(0)
    sliding_times = int(len(sorted_array) / 2)
    
    for i in range(sliding_times):
        sliding_index = i*2
        s_window_head = sorted_array[sliding_index]
        s_window_tail = sorted_array[sliding_index+1]
        if not s_window_head == s_window_tail:
            return s_window_head

# A = [9, 3, 9, 3, 9, 7, 9]
# findUnpairedNum(A)