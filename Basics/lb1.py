# l = [1,2,3,4,5,6,7,8,9,10]
# odd = list(filter(lambda x : x % 2 != 0 , l))
# even = list(filter(lambda y : y % 2 == 0 , l))
# print(odd)
# print(even)

# sq = list(map(lambda x : x**2 , l))
# print(sq)
l = [('One' ,80),('Two',67),('Three',92)]
# sl = list(map(lambda x : x[1]))
sl = sorted(l , key = lambda x : x[1])
print(sl)