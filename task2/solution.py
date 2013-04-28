from collections import defaultdict


def groupby(func, seq):
    groups = defaultdict(list)
    for element in seq:
        groups[func(element)].append(element)
    return groups


def iterate(func):
    identity = lambda x: x
    combine_funcs = lambda x, y: lambda z: x(y(z))
    while True:
        yield identity
        identity = combine_funcs(func, identity)


def zip_with(func, *iterables):
    for group_elements in zip(*iterables):
        yield func(*group_elements)


def cache(func, cache_size):
    cached_results = [[], []]

    def func_cached(*unique_number):
        while True:
            if unique_number in cached_results[0]:
                result_index = cached_results[0].index(unique_number)
                return cached_results[1][result_index]
            else:
                result_func = func(*unique_number)
                cached_results[0].append(unique_number)
                cached_results[1].append(result_func)
                if len(cached_results[0]) > cache_size:
                    del cached_results[0][0]
                    del cached_results[1][0]
                return result_func

    return func_cached
