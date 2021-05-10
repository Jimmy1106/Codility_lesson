# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# <釐清問題>
#   TThis is a 跨越河岸的問題
#   定義:
#    - river: 河岸之間的座標(1~X)
#    - side: 終點與起始點座標分別為X+1和0\

#    - That is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves

#   目標: 
#       透過葉子出現的排列組合尋找到目的地(對岸)的最短路徑
#       (青蛙從座標0開始跳, 欲跳到座標為X+1的對岸(終點))

#   X為river的長度(會踩過的葉子數量), N為陣列長度(全部的葉子數量), A為一Non-empty array(一定會有葉子)
#   e.g.
#   X=5, N=7, A = [1,3,1,4,2,3,5,4]
#       A[0] = 1 (在第0秒時落葉的座標在1)
#       A[1] = 3
#       A[2] = 1
#       A[3] = 4
#       A[4] = 2
#       A[5] = 3
#       A[6] = 5
#       A[7] = 4


# <釐清問題2>
#   走訪一陣列A, 並用一個長度為X的boolean字典紀錄出現過的正整數, 當字典內的所有value皆變成True時(表示葉子橋已建好), 回傳陣列的index.
#   e.g.
#   X=5(河面長度,為程式的終止條件之一), N=7(陣列長度, 其中index代表欲求的秒數), 
#   A = [1,3,1,4,2,3,5,4](儲存每次葉子掉落的座標位置)
#       A[0] = 1  
#       A[1] = 3
#       A[2] = 1
#       A[3] = 4
#       A[4] = 2
#       A[5] = 3
#       A[6] = 5   (在6秒時, 河面上(座標1~5)皆有葉子,即可通過)
#       A[7] = 4

# <定義知識&製作solution><驗證&改進>
#  
# 其它限制:
#   - N and X are integers within the range [1..100,000];
#   - each element of array A is an integer within the range [1..X].
#   - 若陣列走訪完葉子橋還沒建好, 則回傳-1


# Performance: fast > 3 > 4 = 2 > origin

def solution(X, A):
    return findEarliestTime(X,A)

def findEarliestTime(lengthOfBridge:int, leave_falls:list) -> int:
    """ Find the earliest time (index of list) to build up a leaves-bridge. """

    # Init a bridge.
    bridge = {}
    for i in range(lengthOfBridge):
        bridge[i+1] = False
    
    # Travel the list
    for i, pos in enumerate(leave_falls):
        bridge[pos] = True        

        if wasBuilt(lengthOfBridge, bridge):
            return i
    return -1

def wasBuilt(lengthOfBridge, bridge):
    """" Determine a bridge was built or not """
    for i in range(lengthOfBridge):
        if bridge[i+1] == False:
            return False
    return True

def findEarliestTime2(lengthOfBridge:int, leave_falls:list) -> int:
    indexes = []
    for pos in range(1,lengthOfBridge+1):
        # Travel the list
        for i, fell_pos in enumerate(leave_falls):
            if pos == fell_pos:
                indexes.append(i)
                break
            elif pos!=fell_pos and i==len(leave_falls)-1:
                return -1
    return max(indexes)

def findEarliestTimeFast(lengthOfBridge:int, leave_falls:list) -> int:
    # Travel the list & build the table
    # 只需紀錄每個位置最低的秒數, 其中 ,位置介於1~lengthOfBridge之間, 而秒數則介於0~len(leave_falls)-1之間
    OVER_MAX_NUM = -1
    table = [OVER_MAX_NUM]*(lengthOfBridge+1)
    for index, fell_pos in enumerate(leave_falls):
        if table[fell_pos]==OVER_MAX_NUM:
            table[fell_pos] = index

    # target_index = max(table[1:])
    target_index = 0
    for i in range(1,lengthOfBridge+1):
        index = table[i]
        if table[i] == OVER_MAX_NUM:
            return -1
        if index > target_index:
            target_index = index
    return target_index

    # return target_index if target_index!=OVER_MAX_NUM else -1

def findEarliestTime3(lengthOfBridge:int, leave_falls:list) -> int:
    """ Find the earliest time (index of list) to build up a leaves-bridge. """

    # Init a bridge.
    bridge = [False]*(lengthOfBridge+1)
    bridge[0] = True
    
    # Travel the list
    for i, pos in enumerate(leave_falls):
        bridge[pos] = True
        # Determine a bridge was built or not
        if all(bridge):
            return i 
    return -1


def findEarliestTime4(lengthOfBridge:int, leave_falls:list) -> int:
    """ Find the earliest time (index of list) to build up a leaves-bridge. """

    # Init a bridge.
    bridge = {}
    for i in range(lengthOfBridge):
        bridge[i+1] = False
    
    # Travel the list
    for i, pos in enumerate(leave_falls):
        bridge[pos] = True

        # Determine a bridge was built or not
        wasBuilt = True
        for pos in bridge.values():
            if pos == False:
                wasBuilt = False
                break
        if wasBuilt:
            return i
    return -1


import random
import timeit

def runTestCases():

    runSingleTestCase(
        lengthOfBridge=100,
        array_length=10000,
        # func_list=[findEarliestTime, findEarliestTime2, findEarliestTimeFast]
        func_list=[findEarliestTimeFast , findEarliestTime3]
    )

    

def runSingleTestCase(lengthOfBridge, array_length, func_list):
    """ lengthOfBridge: X, array_length: N """

    # Generate test-input
    leave_falls = []
    for i in range(array_length):
        leave_falls.append(random.randint(1,lengthOfBridge))

    for func in func_list:
        # print( "\n("+ str(lengthOfBridge) + "," + str(leave_falls) + ")")
        print("Return: " + str(func(lengthOfBridge, leave_falls)))
        print("Running time: %f" % timeit.timeit(str(func(lengthOfBridge, leave_falls)), "from __main__ import "+func.__name__))

if __name__=='__main__':
    runTestCases()
