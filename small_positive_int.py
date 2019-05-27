def display(in_list):
    temp = None
    for x in in_list:
        if x > 0:
            temp = x
            break

    if temp is None:
        return None
    else:
        for x in in_list:
            if 0 < x < temp:
                temp = x
    return temp


def smallest_positive(in_list):
    small = None
    for num in in_list:
        if num > 0:
            if small is None or num < small:
                small = num
    return small


def smallest_positive_without_none(in_list):
    small = -1
    for num in in_list:
        if num > 0:
            if num < small or small == -1:
                small = num

    return None if small == -1 else small


numbers = [4, -6, 7, 2, -4, 10]

print(smallest_positive_without_none(numbers))
