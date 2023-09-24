T = [2, 1, 2, 5, 7, 6, 9]
max_from_left = T[0]
min_to_right = T[-1]

for i in range(1, len(T)):
    max_from_left = max(max_from_left, T[i])

for i in range(len(T) - 2, -1, -1):
    min_to_right = min(min_to_right, T[i])
print(max_from_left)
print(min_to_right)