import re

data = open('task2.txt', encoding='utf-8').read()

time = list(map(int, re.findall(r'(?<=time=)\d+', data)))
p = len(list(re.findall('out', data)))

print(f'{len(time) + p} packets transmitted, {len(time)} packets received, {p} packets lost')
print(f'Minimum = {min(time)}ms, Maximum = {max(time)} ms, Average={round(sum(time) / len(time))}ms')