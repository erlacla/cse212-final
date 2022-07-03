def find_the_intersection(set_one, set_two):

    intersect = set()
    for n in set_one:
        if n in set_two:
            intersect.add(n)
    return intersect 


set_one = {3, 4, 5}
set_two = {1, 2, 3}
print(find_the_intersection(set_one,set_two))