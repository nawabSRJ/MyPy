import math

nums = [1, 2, 3, 4]
logSum = 0
ans = []

# Step 1: Calculate the total logarithmic sum
for i in nums:
    logSum += math.log(i)

# Step 2: Generate the result array using individual logarithmic differences
for i in nums:
    # Subtract the logarithmic sum of all elements except the current one
    ans.append(math.ceil(math.exp(logSum - math.log(i))))

# Print the result
print(ans)
