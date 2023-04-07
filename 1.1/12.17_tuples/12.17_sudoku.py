with open('input.txt') as file:
    data = [el.strip() for el in file]

n = int(data[0])

arr = []
for i in data[1:]:
    arr_in = []
    for j in i.split():
        arr_in.append(int(j))
    arr.append(arr_in)

flag = True

for i in range(0, len(arr), n):
    for j in range(0, len(arr), n):
        set_a = set()
        for row in arr[i:i+n]:
            for el in row[j:j+n]:
                set_a.add(el)
        flag *= set_a == set(range(1, n**2+1))

print(('Incorrect', 'Correct')[flag])
