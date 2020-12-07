import re

with open('input', 'r') as data:
    __input__ = data.read()


groups = re.split("[\n]+[\n]+", __input__)

ans_by_groups = [g.split('\n') for g in groups]

group_ans = []

for answer_by_person in ans_by_groups:
    ans_by_each_group = []
    for answer in answer_by_person:
        for a in answer:
            if a not in ans_by_each_group:
                ans_by_each_group.append(a)
    group_ans.append(ans_by_each_group)

number_of_ans = [len(g) for g in group_ans]

print("Total Answers: ",sum(number_of_ans))