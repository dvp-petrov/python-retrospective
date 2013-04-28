SIGN_DICT = {'Овен': [[range(21, 32), 3], [range(1, 21), 4]],
             'Телец': [[range(21, 31), 4], [range(1, 21), 5]],
             'Близнаци': [[range(21, 32), 5], [range(1, 21), 6]],
             'Рак': [[range(21, 31), 6], [range(1, 22), 7]],
             'Лъв': [[range(22, 32), 7], [range(1, 23), 8]],
             'Дева': [[range(23, 32), 8], [range(1, 23), 9]],
             'Везни': [[range(23, 31), 9], [range(1, 23), 10]],
             'Скорпион': [[range(23, 32), 10], [range(1, 22), 11]],
             'Стрелец': [[range(22, 31), 11], [range(1, 22), 12]],
             'Козирог': [[range(22, 32), 12], [range(1, 20), 1]],
             'Водолей': [[range(20, 32), 1], [range(1, 19), 2]],
             'Риби': [[range(19, 29), 2], [range(1, 21), 3]]
             }


def what_is_my_sign(day, month):
    return [x[0] for x in SIGN_DICT.items() if
            day in x[1][0][0] and month == x[1][0][1] or
            day in x[1][1][0] and month == x[1][1][1]
            ][0]
