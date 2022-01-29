# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

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
    
