#!/usr/local/bin/python3.9

dataDict = {}

'''
    Currently working with unsorted file
    Should I sort it? If so, where? who does the sorting?
'''

with open('q1mapper.out', encoding='utf-8') as f:
    for line in f:
        category, business = line.strip().split(':')

        if (category in dataDict):
            dataDict[category].append('\'' + business + '\'')
        else:
            dataDict[category] = list(['\'' + business + '\''])

with open('q1reducer.out', 'w') as w:
    for cat in dataDict:
        w.write(cat + ' [')
        w.write(','.join(dataDict[cat]))
        w.write(']\n')

