#!/usr/bin/env python

import re
import argparse
import fileinput

def process_substitutions(e, s, verbose = 0):
    possible_combinations = []
    for item in s.iteritems():
        for n, sub in enumerate(item[1]):
            if verbose > 0:
                print 'Processing substitution', n + 1
            for m in re.finditer(item[0], e):
                i = m.start()
                if verbose > 1:
                    print item[0], '=>', sub, '---', e, '=>', e[0:i] + '(' + sub + ')' + e[i + len(item[0]):],
                new_combination = e[0:i] + sub + e[i + len(item[0]):]
                if new_combination not in possible_combinations:
                    if verbose > 1:
                        print '(new molecule)'
                    possible_combinations = possible_combinations + [ new_combination ]
                    if verbose > 2:
                        print new_combination
                    if verbose > 3:
                        print possible_combinations
                else:
                    if verbose > 1:
                        print
    if verbose > 2:
        print possible_combinations
    return possible_combinations

def process_molecules(m, s):
    c = []
    for n, e in enumerate(m):
        p = process_substitutions(e, s)
        c = c + [ p ]
    return c

def build_tables(d):
    data = {}
    molecules = []
    for i in d:
        a = i.split()
        if len(a) == 3 and a[1] == '=>':
            if a[0] not in data:
                data[a[0]] = []
            data[a[0]] = data[a[0]] + [ a[2] ]
        elif len(a) == 1:
            molecules = molecules + a
    return data, molecules

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', help='Verbose output')
    parser.add_argument('files', metavar='FILE', nargs='*', help='files to read, if empty, stdin is used')
    args = parser.parse_args()

    verbose = args.verbose

    data = []
    for line in fileinput.input(files=args.files):
        data = data + [ line.strip() ]
    substitutions, molecules = build_tables(data)
    if verbose > 2:
        print substitutions, molecules
    results = process_molecules(molecules, substitutions)
    for n, m in enumerate(results):
        print 'Processing molecule', n + 1, 'results in', len(m), 'distince molecules.'

