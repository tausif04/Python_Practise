def swap_first_last(t):
    if len(t) < 2:
        return t
    return t[-1:] + t[1:-1] + t[:1]

my_tuple = (1, 2, 3, 4, 5)
swapped_tuple = swap_first_last(my_tuple)
print("Modified tuple:", swapped_tuple)
