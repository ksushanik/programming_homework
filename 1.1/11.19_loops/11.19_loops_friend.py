def f(n):
    r=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            r.extend([i,n//i])
    return sum(set(r)-set([n]))
def fr(num):
    r=[]
    for x in range(1,num+1):
        y=f(x)
        if f(y)==x and x!=y:
            r.append(tuple(sorted((x,y))))
    return set(r)
print(fr(10_000))