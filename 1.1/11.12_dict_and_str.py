f = open('task.txt', encoding="UTF-8").readlines() 
z={}
for i in f:
    t=i.split(' ')
    z.update({t[0]:(" ".join(t[1:]))})
print(z)
