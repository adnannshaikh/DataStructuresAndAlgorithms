# Google Question
# Given an Array = [2,5,1,2,3,5,1,2,4]
# It should  return 2


arr = [2,5,1,1,5,2,3,5,1,2,4]
def first_rec(arr):
    di = set()
    for i in arr:
        if i in di:
            return i
        di.add(i)
    return None

# print(first_rec(arr))

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j]:
#             print(arr[i])
#             break
#     break

def first_rec_dict(arr):
    di = {}
    for i in arr:
        if i in di:
            return i
        else:
            di[i] = 1
    return None

x = {'a':1}
x.update({'b':True})
print(first_rec_dict(arr))