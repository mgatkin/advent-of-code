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

def cookie_score(ingredients, d, desired_calories = None):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calorie = 0
    for n, ingredient in enumerate(ingredients):
        capacity = capacity + ingredient * d[d.keys()[n]][0]
        durability = durability + ingredient * d[d.keys()[n]][1]
        flavor = flavor + ingredient * d[d.keys()[n]][2]
        texture = texture + ingredient * d[d.keys()[n]][3]
        calorie = calorie + ingredient * d[d.keys()[n]][4]
    if capacity > 0 and durability > 0 and flavor > 0 and texture > 0:
        if desired_calories is not None:
            if calorie == desired_calories:
                return capacity * durability * flavor * texture
            else:
                return 0
        else:
            return capacity * durability * flavor * texture
    else:
        return 0

def mix_4_ingredients(d, desired_calories = None):
    cookie_scores = []
    for ingredient1 in xrange(101):
        if ingredient1 < 100:
            for ingredient2 in xrange(101 - ingredient1):
                if ingredient1 + ingredient2 < 100:
                    for ingredient3 in xrange(101 - ingredient2 - ingredient1):
                        if ingredient1 + ingredient2 + ingredient3 < 100:
                            ingredient4 = 100 - ingredient3 - ingredient2 - ingredient1
                            cookie_scores.append(cookie_score((ingredient1, ingredient2, ingredient3, ingredient4), d, desired_calories))
                        else:
                            ingredient4 = 0
                            cookie_scores.append(cookie_score((ingredient1, ingredient2, ingredient3, ingredient4), d, desired_calories))
                else:
                    ingredient3 = ingredient4 = 0
                    cookie_scores.append(cookie_score((ingredient1, ingredient2, ingredient3, ingredient4), d, desired_calories))
        else:
            ingredient2 = ingredient3 = ingredient4 = 0
            cookie_scores.append(cookie_score((ingredient1, ingredient2, ingredient3, ingredient4), d, desired_calories))
    return max(cookie_scores)

def mix_all_ingredients(d, desired_calories = None):
    cookie = []
    cookie_scores = []
    mix_ingredients(d, cookie, cookie_scores, desired_calories)
    return max(cookie_scores)

def mix_ingredients(d, cookie_ingredients, cookie_scores, desired_calories = None):
    if len(cookie_ingredients) < len(d):
        for amount in xrange(101):
            mix_ingredients(d, cookie_ingredients + [ amount ], cookie_scores, desired_calories)
    else:
        if sum(cookie_ingredients) == 100:
            cookie_scores.append(cookie_score(cookie_ingredients, d, desired_calories))

if __name__ == '__main__':
    ingredients = add_ingredients(fileinput.input())
    if len(ingredients) == 4:
        print 'Best cookie score:', mix_4_ingredients(ingredients)
        print 'Best 500 calorie cookie score:', mix_4_ingredients(ingredients, 500)
    else:
        print 'Best cookie score:', mix_all_ingredients(ingredients)
        print 'Best 500 calorie cookie score:', mix_all_ingredients(ingredients, 500)
