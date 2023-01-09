list1 = [1, 2, 3, 5, 6]
s1 = {1, 2, 3, 5, 6}
s1.add(7)

print(list1)
print(s1)
print(type(list1))
print(type(s1))

s2 = {1, 2, 3, 5, 6, 1, 2}
s2.update([7, 8, 9, 10])
s2.remove(10)
s2.discard(90)

print(s2)