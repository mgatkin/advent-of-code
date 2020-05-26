#!/usr/bin/env python

import re
import argparse
import fileinput

<<<<<<< HEAD
def process_substitutions(e, s):
    if verbose > 0:
        print 'Processing molecule', e
=======

def process_substitutions(e, s, verbose=0):
>>>>>>> feb51af085cb6909c8a67d070b017bff86e0652f
    possible_combinations = []
    number_of_substitutions = sum([len(i) for i in s.itervalues()])
    count = 0
    for item in s.iteritems():
<<<<<<< HEAD
        for n, sub in enumerate(item[1]):
            if verbose > 0:
                print 'Processing substitution', n + 1, '---', item[0], '=>', sub
=======
        for sub in item[1]:
            count = count + 1
            if verbose > 1:
                print 'Processing substitution', count, 'of', number_of_substitutions
>>>>>>> feb51af085cb6909c8a67d070b017bff86e0652f
            for m in re.finditer(item[0], e):
                i = m.start()
                if verbose > 1:
                    print item[0], '=>', sub, '---', e, '=>', e[0:i] + '(' + sub + ')' + e[i + len(item[0]):],
                new_combination = e[0:i] + sub + e[i + len(item[0]):]
                if new_combination not in possible_combinations:
                    if verbose > 1:
                        print '(new molecule)'
                    possible_combinations = possible_combinations + [new_combination]
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
<<<<<<< HEAD
        if verbose > 0:
            print 'Processing', e, 'in', m
        p = process_substitutions(e, s)
        c = c + [ p ]
=======
        if Verbose > 1:
            print 'Processing molecule', n + 1, 'of', len(m)
        subs = process_substitutions(e, s, Verbose)
        c = c + [subs]
    return c


def fabricate_molecules(m, s):
    c = []
    for n, e in enumerate(m):
        i = ['e']
        o = []
        count = 0
        while e not in o:
            if Verbose > 0:
                print 'Processing', len(i), 'molecule(s)'
            o = flatten(process_molecules(i, s))
            i = o
            count = count + 1
            if Verbose > 1:
                print count, 'iterations...'
        c = c + [count]
    return c


'''
def fabricate_molecules(m, s, p):
    c = []
    for n, e in enumerate(m):
        i = ['e']
        o = []
        count = 0
        index = 0
        while e not in o:
            for possible_output in p:
                sub_string_found = False
                length = len(possible_output)
                if len(o) < length:
                    subs = process_substitutions(e, s, Verbose)
                    for sub in subs:
                        sub_length = len(sub)
                        if len(o) < sub_length:
                            continue
                        if o[index:sub_length] is e[index:sub_length]:
                            sub_string_found = True
                            i = sub
                else:
                    if o[index:sub_length] is e[index:sub_length]:
                        sub_string_found = True
                if sub_string_found:
                    break
        c = c + [count]
>>>>>>> feb51af085cb6909c8a67d070b017bff86e0652f
    return c
'''


def fabricate_molecules(m, s):
    c = []
    for n, e in enumerate(m):
         molecule_list = [ 'e' ]
         iterations = 0
         while e not in molecule_list:
             if verbose > 2:
                 print e, 'not in', molecule_list, '---', iterations, 'iteration(s)'
             new_molecule_list = []
             for molecule in molecule_list:
                 new_molecule_list = new_molecule_list + process_molecules(molecule, s)
             iterations = iterations + 1
             molecule_list = []
             for sublist in new_molecule_list:
                 for item in sublist:
                     if item not in molecule_list:
                         molecule_list.append(item)
             #molecule_list = [ item if item not in for sublist in new_molecule_list for item in sublist ]
             #if verbose > 2:
             #    print iterations, molecule_list
         c = c + [ iterataions ]
    return c

def build_tables(d):
    substitutions = {}
    molecules = []
    possible_outputs = []
    for i in d:
        a = i.split()
        if len(a) == 3 and a[1] == '=>':
            if a[0] not in substitutions:
                substitutions[a[0]] = []
            substitutions[a[0]] = substitutions[a[0]] + [a[2]]
            if a[2] not in possible_outputs:
                possible_outputs = possible_outputs + [a[2]]
        elif len(a) == 1:
            molecules = molecules + a
    return substitutions, molecules, possible_outputs


def flatten(l):
    if Verbose > 0:
        print 'Flattening...'
    r = []
    for y in l:
        r = r + [x for x in y]
    #    r = r + [ x for x in y if x not in r ]
    if Verbose > 0:
        print 'Done.'
    return r


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', help='Verbose output')
    parser.add_argument('files', metavar='FILE', nargs='*', help='files to read, if empty, stdin is used')
    args = parser.parse_args()

    Verbose = args.verbose

    Data = []
    for line in fileinput.input(files=args.files):
<<<<<<< HEAD
        data = data + [ line.strip() ]
    substitutions, molecules = build_tables(data)
    if verbose > 2:
        print substitutions, molecules
    #results = process_molecules(molecules, substitutions)
    #for n, m in enumerate(results):
    #    print 'Processing molecule', n + 1, 'results in', len(m), 'distince molecules.'
    results = fabricate_molecules(molecules, substitutions)
    #for n, m in enumerate(results):
    #    print 'Molecule', n + 1, 'fabricated in', m, 'steps.'
=======
        Data = Data + [line.strip()]
    Substitutions, Molecules, PossibleOutputs = build_tables(Data)
    if Verbose > 2:
        print Substitutions, Molecules
    results = process_molecules(Molecules, Substitutions)
    for Number, Molecule in enumerate(results):
        print 'Processing molecule', Number + 1, 'results in', len(Molecule), 'distinct molecules.'
>>>>>>> feb51af085cb6909c8a67d070b017bff86e0652f

#    results = fabricate_molecules(Molecules, Substitutions, PossibleOutputs)
    results = fabricate_molecules(Molecules, Substitutions)
    for Number, Molecule in enumerate(results):
        print 'Molecule', Number + 1, 'created in', Molecule, 'steps.'
