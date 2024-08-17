my_dict={'Vasya':1987, 'Kolya':2000, 'Andrey':1999}
print(my_dict)
print(my_dict.get('Vasya'))
print(my_dict.get('Nadegda'))
my_dict.update({'Serg':1973, 'Vika':1982})
a=my_dict.pop('Kolya')
print(a)
print(my_dict)
my_set={True, 1, 1, True, 0, 2, 3, 6, 6, True, False, 'student'}
print(my_set)#True==1,False==0
my_set.update({'Serg', 1973, 'Vika', 1982})
my_set.remove(True)
print(my_set)