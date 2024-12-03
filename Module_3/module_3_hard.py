data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    x = 0
    for elem in data_structure:
        if isinstance(elem, (list,tuple,set)):
            x +=calculate_structure_sum(elem)


        elif isinstance(elem, dict):
            x +=(calculate_structure_sum(elem.keys()))
            x +=(calculate_structure_sum(elem.values()))


        elif isinstance(elem,str):
            x += len(elem)


        elif isinstance(elem,(int,float)):
            x += elem
    return x




result = calculate_structure_sum(data_structure)

print(result)

