station_number, start_station, finish_station = list(map(int, input().split(" ")))


def metro():
    global finish_station
    delta = abs(finish_station - start_station)
    if delta >= (station_number // 2):
        return station_number - delta - 1
    else:
        return delta - 1


var_1 = metro()
print(var_1)