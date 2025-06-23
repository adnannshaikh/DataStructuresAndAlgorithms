''''
Here i was just trying to figure how to grab keys and assign and implement some operations
on the value of the key
'''
from typing import List

s = 'aabbcdeab'

def c(s):
    di ={}
    for i in s:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    return di

def repeter(s):
    di = {}
    for i in s:
        if i not in di:
            di[i] = [i]
        elif i in di:
            di[i].append(i)
    rp = []
    for v in di.values():
        if len(v)>1:
            rp.extend(v)

    return rp

all_r = repeter(s)

# print(",".join(all_r))
range()

def plusOne( digits: List[int]) -> List[int]:
    if digits[-1] != 9:
        digits[-1] += 1
    else:
        digits[-1] = 1
        digits.append(0)
    return digits

print(plusOne([9]))