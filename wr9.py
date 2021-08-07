x={1,2,3,4}
y={1,4,7,8}
z=x.symmetric_difference(y)
print(z)

print("\nother method")
x={1,2,3,4}
y={1,4,7,8}
x.symmetric_difference_update(y)
print(x)