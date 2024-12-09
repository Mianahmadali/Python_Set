"""Check if a set is a subset of another set.

Check if {1, 2} is a subset of {1, 2, 3, 4}."""
set1 = {1,2}
set2 = {1,2,3,4,}
print(set1.issubset(set2))

# also use <= operator