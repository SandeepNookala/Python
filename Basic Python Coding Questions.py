##multiple two list using lambda and map
#=======================================

t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t1 = (0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

two_tuple = tuple(map(lambda x,y : x*y ,t,t1))

print(two_tuple)