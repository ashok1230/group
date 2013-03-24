class groups:
    def __init__(self,list,size):
	lst=[]
	templist=[]
	count=0
	length=len(list)
	temp=size
	mod=length/size
	if length%size!=0:
	    mod+=1
	for i in range(0,mod):
	    templist=list[count:temp]
	    lst.append(templist)
	    count=temp
	    temp+=count
	print lst
a=groups([1,2,3,4,5,6,7,8,9],3)

	    
	
