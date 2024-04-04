def remove_first_occurrence(t, elem):
    if elem in t:
        index = t.index(elem)
        return t[:index] + t[index+1:]
    else:
        return t
data = [((1, 2, 3), 1),
        ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
        ((2, 4, 6, 6, 4, 2), 9)]

for t, elem in data:
    result = remove_first_occurrence(t, elem)
    print(result)