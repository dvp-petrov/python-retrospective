"""groupby"""
def groupby(func, seq):
    my_dict = dict()
    for x in seq:
        result = func(x)
        if result in my_dict.keys():
            my_dict[result].append(x)
        else:
            my_dict[result] = [x, ]
    return my_dict

"""iterate"""
def combine_funcs(func_one, func_two):
    def composed(*args):
        return func_one(func_two(*args))
    return composed


def iterate(func):
    def identity(input):
        return input

    while True:
        yield identity
        identity = combine_funcs(func, identity)

"""zip_with"""
def zip_with(func, *iterables):
    if len(iterables) == 0:
        iterables = []
        return None
    min_len = 10000
    for x in iterables:
        if min_len > len(x):
            min_len = len(x)
    for i in range(0, min_len):
        params = list()
        for j in iterables:
            params.append(j[i])
        yield func(*params)

"""cache"""
def cache(func, cache_size):
    cached_results = [[], []]

    def func_cached(unique_number):
        while True:
            if unique_number in cached_results[0]:
                too_long_line = cached_results[0].index(unique_number)
                return cached_results[1][too_long_line]
            else:
                result_func = func(unique_number)
                cached_results[0].append(unique_number)
                cached_results[1].append(result_func)
                if len(cached_results[0]) > cache_size:
                    del cached_results[0][0]
                    del cached_results[1][0]
                return result_func

    return func_cached
