n = int(input("n = "))

print(f"Enter {n} array elements:")

arr = [float(input()) for _ in range(n)]

print("Original array: ", arr)

min_neg = None
for num in arr:
    if num < 0:
        if min_neg is None or num < min_neg:
            min_neg = num

if min_neg is not None:
    print("Minimum negative number is:", min_neg)
else:
    print("There are no negative numbers in array.")
