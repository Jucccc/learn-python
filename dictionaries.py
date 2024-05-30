from collections import defaultdict

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.
# * Note: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# - from W3Schools.com

'''
avengers = {1:'Tony',2:'Steve',3:'Thor'}

for k in avengers.keys():
    print('The key',k,'maps to',avengers[k])

ks = avengers.keys()
vals = avengers.values()
print(ks)
print(vals)
print(4 in avengers)
print(3 in avengers)

avengers_two = defaultdict(lambda: 'not an Avenger')
avengers_two[1] = 'Tony'
avengers_two[2] = 'Steve'
avengers_two[3] = 'Thor'

print(avengers_two[1])
print(avengers_two[4])
print(type(avengers_two[4]))
print(avengers_two.get(5,'Hulk'))

print('avengers:', avengers_two)

avengers.update({4:'Hawkeye'})
print(avengers)

other_avengers = avengers.fromkeys((6,7,8,9),'Other avenger')
print(other_avengers)
#other_avengers.fromkeys(('Tony','Steve','Thor'),'Avengers')
#print(avengers)
del(other_avengers[9])
print(other_avengers)
other_avengers.update({5:'Other avenger'})
print(other_avengers)
other_avengers.pop(8,None)
print(other_avengers)
other_avengers = sorted(other_avengers.items())
print(other_avengers)
'''

# Converting lists and dicts

avengers = ['Tony','IronMan']
new_list = list(zip(avengers))
print(new_list)

non_hero_name = ['Tony','Steve','Bruce']
hero_name = ['IronMan','Captain America','Hulk']
zipped_avengers = dict(zip(non_hero_name,hero_name))
print(zipped_avengers)

for n,h in zip(non_hero_name,hero_name):
    print("Name of hero:",n)
    print("Hero name:",h)

new_avengers = dict(zip(avengers[0::2],avengers[1::2]))
print(new_avengers)

#nh_name = list()
#h_name = list()
zipped_avengers_list = list(zip(non_hero_name,hero_name))
print(zipped_avengers_list)
print(type(zipped_avengers_list))
nh_name, h_name = zip(*zipped_avengers_list)
print(nh_name)
print(h_name)

# List Comprehension:
name = ['Tony','Steve']
heros = ['Ironman','Captain']
dict_com = {r:s for r, s in zip(name,heros)}
print(dict_com)

# Merging Dictionaries

a = {'apple':1,'pear':2}
b = {'orange':3}
#merged = {**a,**b} # before version 3.9
#merged = a | b # from version 3.9
a |= b # augmented operator
print('The merged dictionary is:',a)

