set1 = {1, 2, 3, 4, 5,6}
set2 = {3,6,9,12,15}
new_set = {}
temp1={}
s = set1.intersection(set2)
temp1 = set1.union(set2).difference(s)
print(temp1)