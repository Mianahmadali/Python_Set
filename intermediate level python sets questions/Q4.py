"""Remove an element from a set without raising an error if the element does not exist.

Use the discard() method to remove 5 from the set {1, 2, 3, 4, 5}.
"""
set = {1,2,3,4,5}
set.discard(5)
print(set)