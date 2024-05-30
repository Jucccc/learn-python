# A set is a collection which is unordered, unchangeable*, and unindexed. 
# * Note: Set items are unchangeable, but you can remove items and add new items.
# - from W3Schools.com

hero_name = ['IronMan','Captain America','Hulk']
print(type(hero_name))
hero_name_set = set(['IronMan','Captain America','Hulk'])
print(type(hero_name_set))
hero_name_tuple = ('IronMan','Captain America','Hulk')
print(type(hero_name_tuple))
hero_name_set_2 = set(('IronMan','Captain America','Hulk'))
print(type(hero_name_set_2))
print(hero_name_set_2)
hero_name_string = 'IronMan, Captain America, Hulk'
print(type(hero_name_string))
hero_name_set_3 = set(hero_name_string)
print(type(hero_name_set_3))
print(hero_name_set_3)
print(list(hero_name_string))

hero_name_curly = {'IronMan','Captain America','Hulk'}
print('Type of hero_name_curly:',type(hero_name_curly))
empty_hero_name = {}
print('Type of empty_hero_name:',type(empty_hero_name))
empty_hero_name_two = set()
print(type(empty_hero_name_two))

# union - join the two sets

my_set = set(['first item','second item','Hulk'])
print("Join")
print(hero_name_set | my_set)
print(my_set.union(hero_name_set))
print(type(my_set))

#my_set = my_set | ('first item','second item','Hulk') # join set and union with operator function - not working
my_set = my_set.union(('third item','second item','Hulk')) # join set and union with union method - working
print(my_set)

 # intersecion in sets - return the common values

print("Intersection")
print(my_set & hero_name_set)
print(my_set.intersection(hero_name_set))

# difference in sets - return those values which are present in one set but not present in another set

print("Difference")
print(my_set - hero_name_set)
print(hero_name_set.difference(my_set))
print(my_set.difference(hero_name_set))

# simmetric difference - present in either the first set or second set but not in both sets

print("Simmetric Difference")
print(my_set ^ hero_name_set)
print(my_set.symmetric_difference(hero_name_set))
print(hero_name_set.symmetric_difference(my_set))

my_new_set = my_set.copy()
my_new_set.remove('Hulk')
print(my_new_set)
print(my_set)

print(my_new_set.isdisjoint(hero_name_set)) # checks whether the sets have common elements or not
print(my_new_set.issubset(my_set))
print(my_new_set <= my_set)
print(my_set.issubset(my_new_set))

# proper subset ( < )
# .issuperset() ( >= )
# proper superset ( > )
# .add() .remove() .discard() .pop() .clear()
# a.update(b) or a |= b
# a.intersection_update(b) or a &= b [&c...]
# a.difference_update(b) or a -= b [|c...]
# a.simmetric_difference_update(b) or a ^= b [|c...]
# frozenset()

a = frozenset(['Tony','Bruce','Peter'])
print(a)
print(id(a))
b = {'Strange','Thor','Tony'}
a &= b # a = a & b
print(a)
print(id(a))

# Creating a set of sets - not working:
'''
c = set(['Tony'])
d = set(['Steve'])
e = set(['Bruce'])
f = {c,d,e}
print(f)
'''
# a Dictionary key also cannot be a set:
#real_name = ({'Robert','Tony'})
#hero_name = ({'Chris','Steve'})

# but with frozenset it's possible:
real_name = frozenset({'Robert','Tony'})
hero_name = frozenset({'Chris','Steve'})
avengers = {real_name:'Iron Man',hero_name:'Cap'}
print(avengers)

# Set Comprehension - does it remove duplicates if I use curly braces (when creating a set)?

num = [4,3,2,1,5,4,3,2,1,5]
set_com = {n*n for n in num}
print(set_com)
print('Type of set_com:',type(set_com))