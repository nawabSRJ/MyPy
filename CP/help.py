import math

alpha = {
    0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 
    10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 
    19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y'
}

cn = int(input("Enter the Column Number: "))

if cn <= 0:
    print("Invalid column number.")
else:
    ans = ""
    while cn > 0:
        rem = (cn - 1) % 26  # Adjusting for 1-based indexing
        ans = alpha[rem] + ans
        cn = (cn - 1) // 26

    print(ans)
