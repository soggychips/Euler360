import scary_sphere as ss
import cProfile

for num in range(1,51):
    ss.AddMan(num)

print ss.countDict
'''
num = 45

#print "AddMan(%s) = %s\n" % (num,ss.AddMan(num))
#cProfile.run('ss.AddMan(num)')

ss.PrintPointsAlongEquator(num)
'''
