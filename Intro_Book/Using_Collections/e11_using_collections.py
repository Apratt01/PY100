print('johnson' in 'Joe Johnson') # False case sensitive with strings
print('sen' not in 'Joe Johnson') # True 
print('Joe J' in 'Joe Johnson') # True
print(5 in range(5)) # False range does not include the last number
print(5 in range(6)) # True 
print(5 not in range(5, 10)) # False range does not includ the last number
print(0 in range(10, 0, -1)) # False
print(4  in {6, 5, 4, 3, 2, 1}) # True
print({1, 2, 3} in {1, 2, 3}) # False sets are unordered, it can only check for a specific value
print({3, 2} in {1, frozenset({2, 3})}) # True the in operator checks for membership, since
# a set is unordered, {3, 2} is equivalent to {2, 3} and the set is a member of
# the set {1, frozenset({2, 3})}