'''
Problem 360
http://projecteuler.net/problem=360

Given two points (x1,y1,z1) and (x2,y2,z2) in three dimensional space, the Manhattan distance between those points is defined as 
|x1-x2|+|y1-y2|+|z1-z2|.

Let C(r) be a sphere with radius r and center in the origin O(0,0,0).
Let I(r) be the set of all points with integer coordinates on the surface of C(r).
Let S(r) be the sum of the Manhattan distances of all elements of I(r) to the origin O.

E.g. S(45)=34518.

Find S(10^10).

Eq. for a sphere: 
    for center C (q,w,e) and radius r, any point P (x,y,z) is on the sphere, if:
	(x-q)^2 + (y-w)^2 + (z-e)^2 = r^2
	=> r = sqrt(x**2+y**2+z**2)

    in polar coords:
	x = r(cos(theta)*sin(phi))
	y = r(sin(theta)*sin(phi))
	z = r(cos(phi))

'''


def isPointOnSphere(x,y,z,radius):
	return (x**2+y**2+z**2 == radius**2)

def Manhattan(x,y,z):
    return abs(x) + abs(y) + abs(z)

def AddMan(radius):
    points = sorted([Manhattan(x,y,z) for x in range(-radius,radius+1) for y in range(-radius,radius+1) for z in range(-radius,radius+1) if isPointOnSphere(x,y,z,radius)])
    s = "S(%s) = " % radius
    for p in range(0,len(points)):
	s += "%s " % points[p]
	if p != len(points)-1:
	    s += "+ "
    #print "%s = %s" % (s,sum([Manhattan(x,y,z) for x in range(-radius,radius+1) for y in range(-radius,radius+1) for z in range(-radius,radius+1) if isPointOnSphere(x,y,z,radius)]))
    print "Count(S(%s)) = %s" % (radius,len(points))

def AddMan_Gen(radius):
    return sum(Manhattan(x,y,z) for x in range(-radius,radius+1) for y in range(-radius,radius+1) for z in range(-radius,radius+1) if isPointOnSphere(x,y,z,radius))

def PrintPointsAlongEquator(radius):
    for z in range(0,radius+1):
	l = list(((x,y,z) for x in range(-radius,radius+1) for y in range(-radius,radius+1) if isPointOnSphere(x,y,z,radius)))
	if len(l)>0:
	    print "---\nz=%s" % z
	    print "len(l(%s)) = %s" % (z,len(l))
	    print l

