L = [10,20,30,40,50]

print(L)
print(type(L))

L.append(20)
print(L)

print("The term at index 3 is :" ,L[3])

L.remove(10)
print(L)

L.pop()
print(L)

print(L.index(30))

L.append(10)
L.sort()
print(L)

print(L[0:2])

L.reverse()
print(L)