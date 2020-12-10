import json

data = json.loads(open('input.json').read())


def validate_num(num_list):
    valid_num = []
    for x in range(len(num_list)):
        for num in num_list[x+1:]:
            valid_num.append(num_list[x] + num)
    return valid_num


def find_invalid_num(queue):
    while queue:
        try:
            list_25_num = queue[0][0]
            idx_last_num = queue[0][1]
            valid_nums = validate_num(list_25_num)
            idx_next_num = idx_last_num + 1
            if data[idx_next_num] not in valid_nums:
                raise Exception
            else:
                list_25_num.remove(list_25_num[0])
                list_25_num.append(data[idx_next_num])
            queue.append((list_25_num, idx_next_num))
        except Exception:
            return data[idx_next_num]
        finally:
            del queue[0]


def find_weakness(invalid_num):
    for i, num in enumerate(data):
        num_list = []
        num_list.append(num)
        for more_num in data[i+1:]:
            num_list.append(more_num)
            s = sum(num_list)
            if s == invalid_num:
                return min(num_list) + max(num_list)


# Solve Day 9 challenge
preamable_range = 25
preamble_num = data[:preamable_range]

queue = [(preamble_num, preamable_range-1)]

invalid_num = find_invalid_num(queue)

print("Part 2 | Encryption weakness:", find_weakness(invalid_num))