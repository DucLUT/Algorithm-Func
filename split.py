def split(T):
    n = len(T)
    count = 0
    MAX = T[0]
    MIN = T[-1]
    Max_list = []
    Min_list = [MIN]
    for i in range(0,n):
        MAX = max(MAX,T[i])
        Max_list.append(MAX)

    for i in range(n-2,-1,-1):
        MIN = min(MIN,T[i])
        Min_list.append(MIN)

    Min_list.reverse()

    for i in range(0,n-1):
        if Max_list[i]<Min_list[i+1]:
            count+=1

    return count

    

        

    



if __name__ == "__main__":
    print(split([1,2,3,4,5]))       # 4
    print(split([5,4,3,2,1]))       # 0
    print(split([2,1,2,5,7,6,9]))   # 3
    print(split([1,2,3,1]))         # 0