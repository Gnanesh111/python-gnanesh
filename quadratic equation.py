import cmath
a = int(input("enter value of a"))
b = int(input("enter value of b"))
c = int(input("enter value of c"))
 
d = (b**2) - (4*a*c)
 
s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(s1,s2))
