#!/usr/bin/env python

from itertools import permutations
from sys import maxsize
import fileinput

def add_reindeer(d, l):
    if len(l.split()) != 15:
        return
    (name, speed, duration, rest) = [
            l.split()[0],
            int(l.split()[3]),
            int(l.split()[6]),
            int(l.split()[13])
            ] 
    d[name] = (speed, duration, rest)

def race(d, time):
    distance_traveled = [ 0 for i in xrange(len(d)) ]
    time_traveling = [ 0 for i in xrange(len(d)) ]
    time_resting = [ 0 for i in xrange(len(d)) ]
    score = [ 0 for i in xrange(len(d)) ]
    for t in xrange(time):
        for n, deer_info in enumerate(d):
            deer = data[deer_info]
            if time_traveling[n] < deer[1]:
                distance_traveled[n] = distance_traveled[n] + int(deer[0])
                time_traveling[n] = time_traveling[n] + 1
            elif time_resting[n] < deer[2]:
                time_resting[n] = time_resting[n] + 1
            else:
                distance_traveled[n] = distance_traveled[n] + int(deer[0])
                time_traveling[n] = 1
                time_resting[n] = 0
        for n, v in enumerate(distance_traveled):
            if v == max(distance_traveled):
                score[n] = score[n] + 1
    print time, 'second race distance winner:',
    print data.keys()[distance_traveled.index(max(distance_traveled))],
    print max(distance_traveled), 'km'
    print time, 'second race score winner:',
    print data.keys()[score.index(max(score))],
    print max(score), 'points'

if __name__ == '__main__':
    data = {} 
    for n, line in enumerate(fileinput.input()):
        add_reindeer(data, line)
    race(data, 1000)
    race(data, 2503)
