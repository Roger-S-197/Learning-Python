set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2) # (unir)
set5 = set1.difference(set2) # (diferença)
set6 = set1.intersection(set2) # (entre os dois)
set7 = set1.symmetric_difference(set3) # (não mostra o que tem em comum)

print(set4)
print(set5)
print(set6)
print(set7)