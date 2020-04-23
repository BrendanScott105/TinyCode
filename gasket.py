import random
s=101;g,p,q,z,m=[[' 'for a in range(s+1)]for b in range (s+1)],s/2,0,'',100000
for c in range(m):
	g[int(p)][int(q)]=0;r=random.randint(0,2)
	if r==0:p,q=((p-s/2)/2)+s/2,q/2
	if r==1:p,q=p/2,q+((s-q)/2)
	if r==2:p,q=p+((s-p)/2),(q+(s-q)/2)
for y in range(s):
	for x in range(s):z+='0' if g[x][y]==0 else ' ';
	y+=1;print(z);z=''