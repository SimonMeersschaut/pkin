from json import dump
with open('scoef.95a', 'r') as f:
  x = f.read()

x = x.split('\n')
y = [[y for y in z.split(' ') if y != ''] for z in x]
y = [[z for index,  z in enumerate(x) if index in [3]] for x in y]
y = [float(x[0]) for x in y]
with open('natural.json', 'w+') as f:
  dump(y, f)