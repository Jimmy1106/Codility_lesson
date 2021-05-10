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

# def findEarliestTimeFast(lengthOfBridge:int, leave_falls:list) -> int:

#     # # Init a bridge.
#     # bridge = {}
#     # for i in range(lengthOfBridge):
#     #     bridge[i+1] = False

#     for j in range(lengthOfBridge):
#         indexes = []
#         # Travel the list
#         for i, pos in enumerate(leave_falls):
#             if pos == j

# # Generate test-input
# import random
# lengthOfBridge = 10  # X
# array_length =  10000     # N
# leave_falls = []
# for i in range(array_length):
#     leave_falls.append(random.randint(1,lengthOfBridge))
# print( "("+ str(lengthOfBridge) + "," + str(leave_falls) + ")")
