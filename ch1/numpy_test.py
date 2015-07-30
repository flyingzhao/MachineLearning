from numpy import *

print random.rand(4,4)

randmat=mat(random.rand(4,4))
print randmat

invRandmat=randmat.I
print invRandmat
print invRandmat*randmat

print invRandmat*randmat-eye(4)