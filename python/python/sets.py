set1 = {1,4,6,7,8}
set2 = {4,2,7,9,3}

print(set1 | set2 ) #set1.union(set2)

print(set1 & set2 ) #set1.intersection(set2)

print(set1 - set2 ) #set1.difference(set2)

print(set1 ^ set2 ) #set1.symmetric_difference (set2)

s1 ={1,2,3,4}
s2 ={2,4}

print(s1.isdisjoint(s2)) #It will give you true if there's no common element and false if there is..

print(s1 <= s2) #if s1 is subset of s2

print(s1 < s2)  #if s1 is proper subset of s2

print(s1 >= s2) #if s1 is superset of s2

print(s1 > s2) #if s1 is proper superset of s2 