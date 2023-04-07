def arm(n):
    r=0
    sn=str(n)
    l=len(sn)
    for d in sn:
        r+=int(d)**l
        if l > n:
            return False
    if r!=n:
        return False
    return True
lst=[]
for i in range(32000):
    if arm(i):
        lst.append(i)
print(lst)