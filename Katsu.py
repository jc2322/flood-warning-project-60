# This is the workspace for Katsu

from ast import While

from numpy import append
from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
#1D
def rivers_with_station(stations):
    rivers = []
    for station in stations:
        if station.river in rivers:
            pass
        else:
            rivers.append(station.river)
    
    return rivers

def stations_by_river(stations):

    stations_on_each_river = dict()

    for station in stations:
        if station.river in stations_on_each_river:
            stations_on_each_river[station.river].append(station)
        else:
            stations_on_each_river[station.river] = [station]
    return stations_on_each_river

# 1E
def rivers_by_station_number(stations, N):
    rivers = dict()
    for station in stations:
        if station.river in rivers:
            rivers[station.river] += 1 
        else:
            rivers[station.river] = 1
    
    #turns dictionary into list of turple
    N_station = [] 
    for river in rivers:
        N_station.append((river, rivers[river]))
    
    N_station.sort(key=lambda a: a[1], reverse= True)

    N_station_N = N_station[:N]
    #If there are multiple Nth, include
    for i in range(len(stations)):
        if N_station[N-1][1] == N_station[N+i][1]:
            N_station_N.append(N_station[N+i])
        else:
            break

    return N_station_N
