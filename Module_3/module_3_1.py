calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    for i in string:
        return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    for j in [string.lower()]:
        for i in list_to_search:
            if i.lower() == j:
                return True
        return False


print(string_info('skyfall'))
print(string_info('python'))
print(string_info('apple'))
print(is_contains('apple', ['lkgj', 'hfyhek', 'apPle', 'orang']))
print(is_contains('one', ['bapl', 'hfyhek', 'apPle', 'hfyrh']))
print(is_contains('two', ['TWo', 'hfyhek', 'apPle', 'orang']))
print(is_contains('summer', ['bapl', 'SummeR', 'apPle', 'ldfihn']))
print(calls)