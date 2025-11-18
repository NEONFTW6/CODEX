d1 = {1:"Apple",2:"Samsung",3:"Realme",4:"Oneplus"}
print(d1)


print("\n")
d2 = {}
d2["Nike"] = 10000
d2["Adidas"] = 9000
d2["Rebook"] = 5000
d2["Puma"] = 7000
print(d2)
print("Nike:",d2["Nike"])

#getfunction , will not raise an error if key is not present

print(d1.get(1))

print(d1.get(10))

print(d1.get(10,"NA"))

if 10 in d1:
    print(d1[10])
else:
    print("Not available")