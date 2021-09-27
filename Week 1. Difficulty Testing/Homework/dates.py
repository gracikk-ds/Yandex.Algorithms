x, y, z = list(map(int, input().split(" ")))


def dates():
    if (x > 12) or (y > 12) or (x == y):
        return 1
    else:

        return 0


print(dates())
