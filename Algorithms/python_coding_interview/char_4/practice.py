# is와 ==
import copy

a = [1, 2, 3]
# True
print(a == a)
# True
print(a == list(a))
# True
print(a is a)
# False
print(a is list())

# deepcopy
# True
print(a == copy.deepcopy(a))
# False
print(a is copy.deepcopy(a))



