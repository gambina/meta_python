my_list = [1, 2, 3]


def add_to_list(lst, item):
    nl = lst.copy()  # Copy is important in Pure. So it doesn't manipulate the global scope
    nl.append(item)
    return nl
