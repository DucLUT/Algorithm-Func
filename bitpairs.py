def pairs(binary_string):
    distances = []  
    before_position = None
    lst = []
    total_difference = 0

    for i, digit in enumerate(binary_string):
        if digit == '1':
            lst.append(i)
    

    #HASHMAPPPPPPPPPPPPPPPPPPPPP
    count_map = {}
    for num in lst:
        if num in count_map:
            total_difference += count_map[num]
            count_map[num] += num
        else:
            for key in count_map:
                total_difference += abs(key - num)
        count_map[num] = num
    return total_difference


    


if __name__ == "__main__":
    print(pairs("100101"))          # 10
    print(pairs("101"))             # 2
    print(pairs("100100111001"))    # 71