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
#   - 將頭元素後的元素依序加到新陣列中, 最後再將頭元素前的元素(暫存於Buffer)加到新陣列中

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
    # rotation_times %= array_length                        # Fixed: 使用mod記得檢查除數不可為0
    if array_length != 0:
        rotation_times %= array_length

    if rotation_times==0:
        return array

    # if rotation_times == 1:
    #     head = [array[array_length-1]]
    # else:
    #     head = array[(rotation_times-1):]                 # Fixed: 使用Back-slicing記得要加負號
    head = array[(-1*rotation_times):]
        
    tail = array[:(array_length-rotation_times)]

    rotated_array = head + tail

    return rotated_array

import random

def runSolutionByTestCases():

    isAllSucceeded = False

    isAllSucceeded = runCase(
        caseName= "Empty array",
        A=[],
        K=0,
        correct_ans=[]
    )

    isAllSucceeded = runCase(
        caseName= "Small function test, K<N",
        A=[4, 5, 6, 7, 1, 2, 3],
        K=5,
        correct_ans=[6, 7, 1, 2, 3, 4, 5]
    )

    isAllSucceeded = runCase(
        caseName="Small functional tests, K >= N",
        A=[-4, -5, -6, -1, -2],
        K=7,
        correct_ans=[-1, -2, -4, -5, -6]
    )

    isAllSucceeded = runCase(
        caseName="Small random sequence, all rotations, N = 15",
        A=[4, 5, 6, 7, 1, 2, 3, -4, -5, -6, -1, -2, -6, -1, -2],
        K=7,
        correct_ans=[-5, -6, -1, -2, -6, -1, -2, 4, 5, 6, 7, 1, 2, 3, -4]
    )

    isAllSucceeded = verifiedSolution(
        caseName="Maximal N and K",
        A=random.sample(range(-1000, 1000), 100),
        K=66
    )

    print("\nAll cases succeeded!" if isAllSucceeded else "\n")



def runCase(caseName:str, A:list, K:int, correct_ans:list):
    your_ans = solution(A, K)
    if not correct_ans == your_ans:
        print("Fail case: " + caseName)
        print("Correct ans: %s ; Your ans: %s" % (correct_ans,your_ans))
        return False
    return True

def verifiedSolution(caseName:str, A:list, K:int):                                      # 透過反推的方式驗證答案之正確性
    """ Verify solution by a inverted-calucation(rotate the opposite direction)"""
    your_ans = solution(A, K)
    verified_ans = rotate_oppositely(your_ans, K)
    if not A == verified_ans:
        print("Fail case: " + caseName)
        print("Original list: " + str(A))
        print("Verified list: " + str(correct_ans))
        print("Rotated list:  " + str(your_ans))
        return False
    return True

def rotate_oppositely( array:list, rotation_times:int) -> list:
    """ Return a rotated list """
    array_length = len(array)

    if array_length != 0:
        rotation_times %= array_length

    if rotation_times==0:
        return array

    head = array[rotation_times:]
        
    tail = array[:rotation_times]

    rotated_array = head + tail

    return rotated_array

if __name__=='__main__':
    runSolutionByTestCases()  

