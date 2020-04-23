c,d,h=0,0,''
while d!=51:
	l=0;c+=1
	for b in range(9):
		l=l*l-3+.04*c-2j+.08j*d
		if abs(l)>2:h+=' ';break
		if b==8:h+='*'
	if len(h)==99:d+=1;print(h);h,c='',0