def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = ['hello', 2, True]
values_dict = {'a': 10, 'b': 'bye', 'c': False}
values_list_2 = [9, 'one']

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
