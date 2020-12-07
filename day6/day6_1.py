import re

with open('input', 'r') as data:
    __input__ = data.read()


groups = re.split("[\n]+[\n]+", __input__)

ans_by_groups = [g.split('\n') for g in groups]

group_ans = []

for ans_by_group in ans_by_groups:
    ans_yes = []
    for ans in ans_by_group:
        for a in ans:
            if a not in ans_yes:
                ans_yes.append(a)
    group_ans.append(ans_yes)

number_of_ans = [len(g) for g in group_ans]

print("Total Answers: ",sum(number_of_ans))