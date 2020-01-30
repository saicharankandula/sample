d=dict()
n=input('enter number to execute fibbonocci:')
a=int(n)
# def fibfunc(p):
#     if p==0:
#        return 0
#     elif p==1:
#        return 1
#     else :
#        return fibfunc(p-1) + fibfunc(p-2)
# #print(fibfunc(a))
# i=0
# while (i < a) :
#     d[i]=fibfunc(i)
#     i=i+1
# print(d)
d[0]=0
d[1]=1
i=2
while(i<a):
    d[i]=d[i-1]+d[i-2]
    i=i+1
print (d)
