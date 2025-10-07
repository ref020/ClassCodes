#list comprehension
'''
the usual way
cubes = []
for i in rance(10):
    cubes.append(i)
print(cubes)
'''

cubes = [i*i*i for i in range(10)]
print(cubes)

pairs = [[x,y] for x in [1,2,3] for y in [3,1,4] if x != y]
print(pairs)