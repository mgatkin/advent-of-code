#!/usr/bin/env python

from itertools import permutations
from sys import maxsize
import fileinput

def add_ingredients(it):
    data = {} 
    for n, line in enumerate(it):
        add_ingredient(data, line)
    return data

def add_ingredient(d, l):
    if len(l.split()) != 11:
        return
    (name, capacity, durability, flavor, texture, calories) = [
            l.split()[0][:-1],
            int(l.split()[2][:-1]),
            int(l.split()[4][:-1]),
            int(l.split()[6][:-1]),
            int(l.split()[8][:-1]),
            int(l.split()[10])
            ] 
    d[name] = (capacity, durability, flavor, texture, calories)

def cookie_score(ingredients, d):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for n, ingredient in enumerate(ingredients):
        capacity = capacity + ingredient * d[d.keys()[n]][0]
        durability = durability + ingredient * d[d.keys()[n]][1]
        flavor = flavor + ingredient * d[d.keys()[n]][2]
        texture = texture + ingredient * d[d.keys()[n]][3]
    if capacity > 0 and durability > 0 and flavor > 0 and texture > 0:
        return capacity * durability * flavor * texture
    else:
        return 0

def mix_ingredients(d):
    cookie_scores = []
    for ingredient1 in xrange(101):
        if ingredient1 < 100:
            for ingredient2 in xrange(101 - ingredient1):
                if ingredient1 + ingredient2 < 100:
                    for ingredient3 in xrange(101 - ingredient2 - ingredient1):
                        if ingredient1 + ingredient2 + ingredient3 < 100:
                            ingredient4 = 100 - ingredient3 - ingredient2 -ingredient1
                            cookie_scores.append(cookie_score((ingredient1, ingredient2, ingredient3, ingredient4), d))
                        else:
                            ingredient4 = 0
                            cookie_scores.append(cookie_score((ingredient1, ingredient2, ingredient3, ingredient4), d))
                else:
                    ingredient3 = ingredient4 = 0
                    cookie_scores.append(cookie_score((ingredient1, ingredient2, ingredient3, ingredient4), d))
        else:
            ingredient2 = ingredient3 = ingredient4 = 0
            cookie_scores.append(cookie_score((ingredient1, ingredient2, ingredient3, ingredient4), d))
    #print len(cookie_scores)
    return max(cookie_scores)

if __name__ == '__main__':
    ingredients = add_ingredients(fileinput.input())
    print 'Best cookie score:', mix_ingredients(ingredients)
