#declare a tuple
x = ("Beata", 62, True)
y = tuple (["Gary", 23, False])
#print tuples
print(x)
print(y)
print(x[2])
print(y[0:2])
#cant change individual items (immutability)
#x[1] += 1

#concatenate Tuples(add them)
z = x + y
print(z)
print(x)
print(y)

#use min and max function on tuples
t = (74, 35, 1, 83, 65, 62)
print(max(t))
print(min(t))

#fixing errors on tuples
print(x)
l1 = list(x)
l1[2] = False
x = tuple(l1)
print(x)


