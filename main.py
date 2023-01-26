

one = 'Python is the best programming language in the world'
podst=one[5: -7]
print(one)
print(podst)
two = 'Guido van Rossum is the benevolent dictator for life'
twopodst  = two[2::3]
print(twopodst)
three = 'You have a problem with authority, Mr. Anderson.'
mnog = list(three)

print(mnog)
dir(three)
aa = set(three)
aaa = sorted(aa)
print(aaa)
t = len(aaa)
print(t)
c=list()
for i in range(t): c.append(three.count(aaa[i]))
print(c)
d = {}

d = dict.fromkeys(aaa, 1)
for e in range(t): d[aaa[e]] = c[e]
print(e)
print(d)

