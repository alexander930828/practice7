# strs = []
#
# for char in s:
#     if char.isalnum():
#         strs.append(char.lower())
#
#
# while len(strs) > 1:
#     if strs.pop(0) != strs.pop():
#         return False
import collections

def ispalindrome(s: str) -> bool:
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


print(ispalindrome("race a ecar"))


# def ispalindrome1(self, s: str) -> bool:
#     # 자료형 데크로 선언
#     strs: deq = collections.deque()

