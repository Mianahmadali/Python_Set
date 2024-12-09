"""Check if a set is a superset of another set.

Check if {1, 2, 3, 4} is a superset of {1, 2}."""

set1 = {1,2,3,4}
set2 = {1,2}
print(set1.issuperset(set2))

#  also use >= operator