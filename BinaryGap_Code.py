# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Binary gap:
#   任意連續二進位值為0的位元, 且這些位元被二進位值為1的位元圍住
#   e.g. 
#       9    ->     1001     -> 2    -> 2
#       529  ->  1000010001  -> 4,3  -> 4
#       1041 ->  10000010001 -> 5,3  -> 5
#       20   ->      10100   -> 1    -> 1
#       32   ->     100000   -> None -> 0
# <Flow>
#   Int2binary -> findGap -> determineMaxGapLength

# <其他條件>
#   - 正整數N的range在1~2147483647間

def solution(N):
    bin_str = Int2binary(N)

    gaps = findGap(bin_str)

    maxGaplength = determineMaxGapLength(gaps)

    return maxGaplength


def Int2binary(n:int) -> str:
    """ Return a binary string """
    bin_str = bin(n)[2:]
    return bin_str


def findGap(bin_str:str) -> list:
    """ Return a list of gap length """
    bin_gaps = []
    
    cnt = 0
    for c in bin_str:
        if c == "1":
            if cnt!=0:
                bin_gaps.append(cnt)
            cnt = 0
        else:           # c == "0"
            cnt += 1

    return bin_gaps


def determineMaxGapLength(gaps:list) -> int:
    """ Return max item of the list """
    if len(gaps)==0:
        return 0
    return max(gaps)
