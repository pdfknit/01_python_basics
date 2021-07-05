src = (2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11)


def no_repeat_generator(src_list):
    for num in src_list:
        i = 0
        for num_02 in src_list:
            if num_02 == num:
                i += 1
        if i == 1:
            yield num


print(list(no_repeat_generator(src)))
