def loops_3():

    final_list = []

    for x in range(10):
        list_number = []
        for y in range(10):
            list_number.append('1')
        final_list.append(list_number)
    return final_list