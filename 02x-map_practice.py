# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)


fruits = ["apple", "orange", "pear"]

a = map(len, fruits)
b = map(lambda x: x.upper(), fruits)
c = map(lambda x: x[::-1], fruits)
d = map(lambda x: x[:2], fruits)
e = map(lambda z: str(z), [1,2,3,4,5,6,7,8,9,10,11] )
f = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(list(a))
print(list(b))
print(list(c))
print(list(d))
print(list(e))
print(tuple(f))
