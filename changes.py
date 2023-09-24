def changes(A):
    changes = 0
    length = len(A)
    if length < 2:
        return changes

    counts = [] 
    current_count = 1  

    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            current_count += 1
        else:
            if current_count > 1:
                counts.append(current_count)
            current_count = 1

    
    if current_count > 1:
        counts.append(current_count)
    
    for i in counts:
        changes += int(i/2)

    return changes



if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2




