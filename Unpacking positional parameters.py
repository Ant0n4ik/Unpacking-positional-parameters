def print_params(a = 1, b = 'str', c = True):
    print(a, b, c)
print_params()
print_params(10)
print_params(10, 'Да')
print_params(10, 'Да', False)
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [8, 'No', False]
values_list = {'a': 1.1, 'b': 'Hloo World', 'c': [8, 7, 2]}
print_params(*values_list)
print_params(**values_list)
values_list_2 = [81, 'str_']
print_params(*values_list_2, 22.5)