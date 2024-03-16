def subsets(arr):
    ans = []   
    # power set
    n = len(arr)
    total_subsets = 2 ** n # formula

    for i in range(total_subsets):
        current_subset = [] # reset 
        for j in range(n):
            if (i // (2 ** j)) % 2 != 0:
                current_subset.append(arr[j])
        ans.append(current_subset)

    return ans

arr = [1,2,3]
result = subsets(arr)
print(result)
