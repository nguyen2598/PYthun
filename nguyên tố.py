	# your code goes here
import math
t=int(input())
while t>0:
	a= int(input());
	if a<2:
	    print("NO");
	else :
	    kt=0;
	    
	    for i in range(2,int(math.sqrt(a))+1) :
	        if a%i==0: 
	            kt=1;
	            break;
	    if kt==0:
	        print("YES")
	    else :
	        print("NO")
	t-=1