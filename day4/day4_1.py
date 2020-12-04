import re

with open('input', 'r') as _input:
    passport_data = _input.read()

# Passport in the input data are visually separated by blank lines
# Split the data according to that rule and store into a list
passports_separated = re.split("[\n]+[\n]+", passport_data)

# list of passport with key:value pairs
passport_list = []

for i in passports_separated:  
    passport = dict()
    item = re.split('[\n ]+', i)
    for pair in item:
        passport[pair.split(':')[0]] = pair.split(':')[1]
    passport_list+=[passport]

field_list_wo_cid = sorted(['byr','iyr','eyr','hgt','hcl','ecl','pid'])  # --> sorted key list
field_list_to_check = []

valid_passport_list = []

for i in passport_list:
    sorted_key = sorted(i.keys())
    if 'cid' in sorted_key:
        sorted_key.remove('cid')
    check = all(item in sorted_key for item in field_list_wo_cid)
    if check == True:
        valid_passport_list.append(i)

print('Number of valid passport:',len(valid_passport_list))