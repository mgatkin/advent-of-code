#!/usr/bin/env python

from itertools import permutations
from sys import maxsize
import fileinput

def add_hop(d, l):
    (key, item, value) = [ l.split()[0], l.split()[2], l.split()[4] ] 
    if d.has_key(key):
        d[key][item] = value
    else:
        d[key] = { item: value }
    if d.has_key(item):
        d[item][key] = value
    else:
        d[item] = { key: value }

def distance(d, departure, arrival):
    return int(d[departure][arrival])

def shortest(d):
    shortest_trip = maxsize
    for trip in permutations(d):
        trip_distance = 0
        for hop in xrange(len(trip) - 1):
            trip_distance = trip_distance + distance(d, trip[hop], trip[hop + 1])
        if trip_distance < shortest_trip:
            shortest_trip = trip_distance
    print shortest_trip, trip

def longest(d):
    longest_trip = 0
    for trip in permutations(d):
        trip_distance = 0
        for hop in xrange(len(trip) - 1):
            trip_distance = trip_distance + distance(d, trip[hop], trip[hop + 1])
        if trip_distance > longest_trip:
            longest_trip = trip_distance
    print longest_trip, trip

if __name__ == '__main__':
    data = {} 
    for n, line in enumerate(fileinput.input()):
        add_hop(data, line)
    shortest(data)
    longest(data)
