import sys

if(len(sys.argv)!=3):
    print "i need 2 args in the form <start> <end>"
    sys.exit(2)

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
print map(F, range(int(sys.argv[1]),int(sys.argv[2])))
