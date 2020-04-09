'''
scientists = [{'name': 'Ada', 'field' : 'math', 'born': 1815, 'nobel' : False},
              {'name': 'Emmy', 'field' : 'math', 'born': 1882, 'nobel' : False}
            ]

print(scientists)
'''
import collections
from pprint import pprint

Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])

#print (Scientist)

ada = Scientist(name = 'Ada', field = 'math', born = 1815, nobel = False)
emmy = Scientist(name = 'Emmy', field = 'math', born = 1882, nobel = False)
marie = Scientist(name = 'Marie', field = 'physics', born = 1867, nobel = True)
tu = Scientist(name = 'Tu', field = 'chemistry', born = 1930, nobel = True)
yo = Scientist(name = 'Yo', field = 'chemistry', born = 1939, nobel = True)
vera = Scientist(name = 'Vera', field = 'astronomy', born = 1928, nobel = False)
sally = Scientist(name = 'Sally', field = 'physics', born = 1951, nobel = False)

scientists = (ada,)

scientists += (emmy,marie,tu, yo, vera, sally, )

name = 'Sudip'

sudip = Scientist(name = name, field = 'physics', born = 1975, nobel = False)

scientists += (sudip,)

pprint(scientists)

'''
Filter
'''
fil = filter(lambda x: x.nobel is True, scientists)

for x in fil:
    print("------")
    pprint(x)

fil = tuple(filter(lambda x: x.nobel is True, scientists))

pprint(fil)

print ("======")
pprint(tuple (filter(lambda x: x.field == 'physics' and x.nobel, scientists)))

def nobel_filer(x):
    return x.nobel is True

print ("*******")
pprint(tuple (filter(nobel_filer, scientists)))

print ("List++++++++++")
pprint([x for x in scientists if x.nobel is True])

print ("Convert List to Tuple+++++++++")
pprint(tuple([x for x in scientists if x.nobel is True]))

print ("Tuple Generator, ad hoc iterator i.e. memory efficient+++++++++")
pprint(tuple(x for x in scientists if x.nobel is True))

'''
Map(Used for comuting formating etc..)
'''

names_and_ages = tuple(map(
    lambda x: {'name' : x.name, 'age': 2020 - x.born},
    scientists
))

pprint(names_and_ages)

print ("Map List")
pprint([{'name': x.name, 'age': 2020 - x.born}
 for x in scientists])

print ("Map tuple")
pprint(tuple ([{'name': x.name, 'age': 2020 - x.born}
 for x in scientists]))

print ("Map generator")
pprint(tuple ({'name': x.name, 'age': 2020 - x.born}
 for x in scientists))



from functools import reduce
'''
Reduce Function
'''
reduce
