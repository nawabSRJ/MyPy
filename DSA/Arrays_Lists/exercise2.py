# this exercise is provided by codebasics on YT
# * URL of the exercise - https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md 

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append('black panther')
print(heros)

# *putting black panther after hulk

last = heros.pop()  # * Alternate : heros.remove('black panther')
heros.insert(3,last)

print("Updated List :",heros)

heros.remove('thor')
heros.remove('hulk')
print("\nList after removal :",heros)

heros.insert(1,"doctor strange")
print(heros)

# * Alternate of replacing thor and hulk w/ doctor strange

# * heros[1:3] = ['doctor strange']

heros.sort()
print("After sorting in alphabetical order : ", heros)