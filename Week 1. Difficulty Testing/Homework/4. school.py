import math
stdnts_nmbr = int(input())
coords = list(map(int, input().split(" ")))


def mean_func_1():
    if stdnts_nmbr == 0:
        return 0
    sum_coords = 0
    for i in coords:
        sum_coords += i
    position = math.ceil(sum_coords / stdnts_nmbr)

    total_distance = sum([abs(i-position) for i in coords])
    print("position", position)
    print("distance", total_distance, "\n")
    return position


def mean_func_2():
    if stdnts_nmbr == 0:
        return 0
    if stdnts_nmbr == 1:
        return coords[0]

    position = coords[math.ceil(stdnts_nmbr / 2) - 1]
    total_distance = sum([abs(i - position) for i in coords])
    print("position", position)
    print("distance", total_distance)
    return position


position_1 = mean_func_1()
position_2 = mean_func_2()
