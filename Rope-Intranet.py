f=open(r"C:\Users\Prasad\Desktop\A-large-practice (2).in","r")
fo=open(r'C:\Users\Prasad\Desktop\hi.txt',"w")
N=int(f.readline())
i=0
count=0;
while(i<N):
    j=0
    lst=[]
    no=int(f.readline())
    while(j<no):
        a,b=(f.readline()).split()
        a,b=int(a),int(b)
        lst.append([a,b])
        j=j+1
    
    k=0
    count=0
    while(k<(len(lst)-1)):
        m=k+1
        while(m<len(lst)):
              if(((lst[k][0]<lst[m][0])and(lst[k][1]>lst[m][1])) or ((lst[k][0]>lst[m][0])and(lst[k][1]<lst[m][1])) ):
                  count=count+1
              m=m+1
        k=k+1
    fo.write("Case #"+str(i+1)+": "+str(count))
    fo.write('\n')
    i=i+1;
fo.close()

