def f(n, s, lst1):
    r=int(n)
    for j in range(2, int(r**0.5)+1):
        if r%j==0:
            return[]
    if s==0:
        return lst1
    if r not in lst1:
        lst1.append(r)
    s-=1
    n=n[1:]+n[0]
    return f(n,s,lst1)
n=1_000_000
lst=[]
for n in range(2,n+1):
    if n in lst:
        n=n+1
    n=str(n)
    s=len(n)
    lst+=f(n,s,lst1=[])
print(len(lst))