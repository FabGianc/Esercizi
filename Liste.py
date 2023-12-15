"""
Esempio con liste
"""

s1 = 'Hello'
print(s1)
s2 = 'World'
print(s2)
l1 = list(s1)
print(l1)
l2 = list(s2)
print(l2)
l1.append(' ')
print(l1)
l2.append('!')
print(l2)
l1.extend(l2)
print(l1)
l1.pop(6)
print(l1)
l1.insert(6, 'w')
print(l1)
l3 = []
print(l3)
l3.extend(l1[6:9])
print(l3)
l3.append('k')
print(l3)