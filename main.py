import time


def end_to_end_numbering(n_customers):
    dict_of_sum = {}
    for id in range(n_customers):
        num = 0
        while id > 0:
            num += id % 10
            id //= 10
        if num not in dict_of_sum:
            dict_of_sum[num] = 1
        else:
            dict_of_sum[num] += 1

    return dict_of_sum


def index_numeration(n_customers, n_first_id):
    dict_of_sum = {}
    for id in range(n_first_id, n_customers + n_first_id):
        num = 0
        while id > 0:
            num += id % 10
            id //= 10
        if num not in dict_of_sum:
            dict_of_sum[num] = 1
        else:
            dict_of_sum[num] += 1
    return dict(sorted(dict_of_sum.items()))


start_time = time.time()
print(end_to_end_numbering(9999999))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(index_numeration(9999999, 123))
print("--- %s seconds ---" % (time.time() - start_time))