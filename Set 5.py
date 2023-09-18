A = {'a', 'b', 'c', 'd'}
N = {'c', 'd', 'e' }
F = {}
print(A.symmetric_difference(N))
print(N.symmetric_difference(A))
print(A.symmetric_difference(F))
print(N.symmetric_difference(F))