# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# <釐清問題>
#   計算從起始座標(X=10)抵達某一座標(Y=85)至少需要多少個位移(D=30)
#   e.g.
#       X = 10 (起始座標)
#       Y = 85 (須越過的target)
#       D = 30 (每次跳躍的distance)
#
#       最終位置 = 10+(30*3)= 100 > 85(Y的位置),
#       表示X需要跳3次才能跳過Y, 故return3


# <定義知識&製作解決方案>
#   用三個變數做算術運算,並在X未移後的最終位置>Y的位置時, return 跳躍次數的counter.

# <驗證&改進>
#   可能的測資:
#       - (1,1,1)
#       - (10, 1000000000, 11) -> TIMEOUT ERROR (Killed. Hard limit reached: 5.000 sec.)
#       - (1,1000000000,1)
#       - (31, 44648891, 13) # print(31+13*3434528)

#   需減少運算時間:
#       - 

#   其他限制:
#       X, Y and D are integers within the range [1..1,000,000,000] (皆為正整數)
#       X ≤ Y (X只會右移動或不移動)

def solution(X, Y, D):
    return countMinNumOfJumpsFast(X,Y,D)

def countMinNumOfJumps(start:int, target:int, distance:int) -> int:
    final_position = start
    cnt_jumps = 0
    while final_position<target:
        final_position += distance
        cnt_jumps += 1
    return cnt_jumps

def countMinNumOfJumpsFast(start:int, target:int, distance:int) -> int:
    # 核心:
    #   起始位置+ (位移*位移次數)= 最終位置 > Y的位置
    #
    # - 減少迴圈運算改善效能

    tmp = target - start
    jumps = int( tmp / distance)
    if tmp%distance != 0:             # 若整除則終點位置=Y, 反之則需再多走一步
        jumps += 1
    
    return jumps

# When using:
#    jumps = round(tmp/distance + 0.5)
# Get the wrong answer:
# Your test case: [1, 1000000000, 1]
# Returned value: 1000000000
# <Idea>
#   可能出現的狀況:
#       - tmp%distance = remainder that lower than distance, the answer should be plus 1
#       - tmp%distance = no remainder, the answer what we want.
#
#   故round(tmp/distance + 0.5) 不適用於此處