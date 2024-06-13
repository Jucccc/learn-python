# Iterable objects has "__iter__" magic functions
# Iterator object has a "__next__" function

a = [4,3,2,1] # Lists are iterables
print(dir(a))
#print(next(a)) # TypeError: 'list' object is not an iterator
b = iter(a) # make it to be an iterator
print(dir(b))
print(next(b))