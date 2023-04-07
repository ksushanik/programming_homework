a=int(input('Введите левую границу: '))
b=int(input('Введите правую границу: '))
k=0
res=0
for num in range(a,b+1):
    if num%3==0:
        res+=num
        k+=1
print(res/k)