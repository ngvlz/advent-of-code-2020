import json

data = json.loads(open('input.json').read())

def check_sum(data, k):
    for x in range(len(data)):
        for y in range(x+1, len(data)):
            if data[x] + data[y] == k:
                return data[x], data[y]

print(check_sum(data, 2020))
