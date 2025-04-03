arr = [1, 2, 4, 5]
arr2 = [9, 20]

arr2.extend(arr)
arr2.sort()
n = len(arr2)
median = 0
if n % 2 == 0:
    mid1 = arr2[n // 2 - 1]
    mid2 = arr2[n // 2]
    median = (mid1 + mid2) / 2
else:
    median = [n // 2]
print(median)