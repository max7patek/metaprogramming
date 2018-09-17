
def generator(prompt):
    string = input(prompt)
    while '$break' not in string:
        if '$' not in string:
            yield string
        else:
            for dollar in generator('$ = '):
                yield string.replace('$', dollar)
        string = input(prompt)
    print('breaking')
    raise StopIteration


for i in generator('input: '):
    print(i)
