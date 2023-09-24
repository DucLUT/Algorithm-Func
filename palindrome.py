def changes(A):
    changes = 0
    length = len(A)
    if length < 2:
        return changes

    counts = {}
    for i in A:
        if i in counts:
            counts[i]+=1
        else:
            counts[i]=1
    list1 = list(counts.values())
    print(list1)

changes([1, 1, 1, 1, 1])