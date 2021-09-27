d = int(input())
x, y = list(map(int, input().split()))


def point_x():
    if (0 <= x <= d) and (0 <= y <= d):
        if (d - x - y) >= 0:
            return 0

    distance_a = abs(0 - x) + abs(0 - y)
    distance_b = abs(d - x) + abs(0 - y)
    distance_c = abs(0 - x) + abs(d - y)

    if (distance_a <= distance_b) and (distance_a <= distance_c):
        return 1
    elif distance_b <= distance_c:
        return 2
    else:
        return 3


print(point_x())
