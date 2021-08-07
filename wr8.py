x={1,2,3,4}
y={1,4,7,8}
z=x.difference(y)
print(z)

print("\nother method")
x={1,2,3,4}
y={1,4,7,8}
x.difference_update(y)
print(x)