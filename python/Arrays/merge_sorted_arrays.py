a = [0,3,4,31]
b = [4,6,30]
def mergeSortedArrays(a,b):
    for i in range(len(b)):
        a.append(b[i])

    return sorted(a)



print(mergeSortedArrays(a,b))


