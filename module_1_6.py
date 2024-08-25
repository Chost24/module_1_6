my_dict = {'Ben': 88002504907, 'Richard': 88002305703, 'Hank': 89004705873}
print(my_dict)
print(my_dict['Hank'])
print(my_dict.get('Max'))
my_dict.update({'Anton': 880085749328,
                'Jack': 88002845923})
a = my_dict.pop('Anton')
print(my_dict)
print(a)
my_set = {1, 2, True, 'Pol', 2, 1, True}
print(my_set)
my_set.add(False)
my_set.add(4)
my_set.remove(1)
print(my_set)

