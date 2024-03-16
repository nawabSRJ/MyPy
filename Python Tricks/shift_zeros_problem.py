# Shift Zeros Problem
# ? Question - Take a list with numerica elements and shift all the zeros to the right and non-zeros to the left, also maintain the order in which non-zero elements are arranged in the original list
import time
import random
# * Naive Method :  TC -> O(n^2)

# def solution(lst):
#     for i in lst:   # * O(n)
#         if i == 0:
#             lst.remove(i)   # * O(n)
#             lst.append(0)
#     return  lst

# lst = [random.randint(0,2) for _ in range(7)]
# # print(solution(lst))
# start = time.time()
# ans = solution(lst)
# stop = time.time()
# print(ans)
# print('Total Time taken : ', start - stop)


# * Efficient Alternative : TC -> O(n)

def solution(lst):
    t = []
    z = 0
    for i in lst:       # * O(n)
        if i != 0:
            t.append(i)  # * O(1)
        else :
            z += 1      # * O(1)
    t.extend(z * [0])   # * O(n)
    return t

lst = [random.randint(0,2) for _ in range(7)]
# print(solution(lst))
start = time.time()
ans = solution(lst)
stop = time.time()
print(ans)
print('Total Time taken : ', start - stop)


# * Note : An observeable and significant difference in execution time will reflect only with large dataset 