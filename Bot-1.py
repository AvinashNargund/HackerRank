#Solution to https://www.hackerrank.com/challenges/saveprincess
def displayPathtoPrincess(n,grid):
#print all the moves here
    left=1
    right=1
    up=0
    down=0
    x=0
    y=0

    for i in xrange(0,m):
        try:
            y= grid[i].split("-").index('p')
        except ValueError:
            x=0
        else:
            x=i

    k=l=(m-1)/2

    while(k>=0 and l>=0 and k<m and l<m):
		if(k==x and l==y):
		    break
		if(x==0 and y==0):
		    if(left==1):
		        print "UP"
		        k=k-1
		        left=0
		        up=1
		        continue
		    if(up==1):
		        print "LEFT"
		        l=l-1
		        left=1
		        up=0
		        continue
		if(x==0 and y==m-1):
		    if(right==1):
		        print "UP"
		        k=k-1
		        right=0
		        up=1
		        continue
		    if(up==1):
		        print "RIGHT"
		        l=l+1
		        right=1
		        up=0
		        continue
		if(x==m-1 and y==0):
		    if(left==1):
		        print "DOWN"
		        k=k+1
		        left=0
		        down=1
		        continue
		    if(down==1):
		        print "LEFT"
		        l=l-1
		        left=1
		        down=0
		        continue
		if(x==m-1 and y==m-1):
		    if(right==1):
		        print "DOWN"
		        k=k+1
		        right=0
		        down=1
		        continue
		    if(down==1):
		        print "RIGHT"
		        l=l+1
		        right=1
		        down=0
		        continue

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
