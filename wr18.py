s1= {1,2,3,4,5}
s2= {4,5,6,7,8}
x=s1.difference(s2)
print(x)

s1= {1,2,3,4,5}
s2= {4,5,6,7,8}
x=s2.difference(s1)
print(x)

s1= {1,2,3,4,5}
s2= {4,5,6,7,8}
s1.difference_update(s2)
print(s1)


s1= {1,2,3,4,5}
s2= {4,5,6,7,8}
s2.difference_update(s1)
print(s2)