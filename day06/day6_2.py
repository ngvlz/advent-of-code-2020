import re

with open('input', 'r') as data:
    __input__ = data.read()

groups = re.split("[\n]+[\n]+", __input__)
ans_by_groups = [g.split('\n') for g in groups]
count = 0

for ans_by_group in ans_by_groups:
    ans_yes = set(ans_by_group[0])
    for other_ppl_ans in ans_by_group[1:]:
        ans_yes = ans_yes.intersection(other_ppl_ans)
    count += len(ans_yes)

print("Total Answers: ",count)
