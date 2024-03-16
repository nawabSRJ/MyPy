def less_than(lst , k):
    new_lst = [ x for x in lst if x < k]
    return new_lst

prev = [1,2,3,4,5,6,7]
ans = less_than(prev , 6)
print(ans)
    