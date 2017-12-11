import sys

if(len(sys.argv)>2):
    print "give me 1 integer, no extra args"
    sys.exit(2)
num = int(sys.argv[1])
factorial=1

if(num<0):
    print "no negative nums"
    sys.exit(2)

elif num==0:
    print 1

else:
    for i in range(1,num+1):
        factorial=factorial*i
    print num,": ",factorial
