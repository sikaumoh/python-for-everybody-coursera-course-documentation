# Building a dictionary from scratch
purse = dict()  # OR purse = {}
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
# print(purse)
# prints out {'money': 12, 'candy': 3, 'tissues': 75}

# counting a list with a dictionary
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
# print(counts)
# prints out {'csev': 2, 'cwen': 2, 'zqian': 1}

# Better way to write the code
for name in names:
    counts[name] = counts.get(name, 0) + 1

# Exercise 1
# Mostly used Email
filename = '../misc/mbox-short.txt'
data = open(filename)
counter = dict()
# counts email per line
for line in data:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    email = line.split()[1]
    counter[email] = counter.get(email, 0) + 1

# Every dictionary consist of a key and its value
# dict = {key: value}
# for v in dict.values(): gives out the value
# for k in dict.keys(): gives out the key
# for k, v in dict.items(): gives out both key and value
# Check list comprehension to understand this next step
def checker():
    list = [v for v in counter.values()]
    for k in counter.keys():
        if counter.get(k) == max(list): print('Mostly Used:', k)
        if counter.get(k) == min(list): print('Rarely Used:', k)

checker()
