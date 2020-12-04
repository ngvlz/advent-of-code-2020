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

#* sorted key list: ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
valid_passport = [p for p in valid_passport_list if (
                        (p[field_list_wo_cid[0]].isdigit() and len(p[field_list_wo_cid[0]])==4 and 1920 <= int(p[field_list_wo_cid[0]]) <= 2002)
                    and (p[field_list_wo_cid[1]] in ['amb','blu','brn','gry','grn','hzl','oth'])
                    and (p[field_list_wo_cid[2]].isdigit() and len(p[field_list_wo_cid[2]])==4 and 2020 <= int(p[field_list_wo_cid[2]]) <= 2030)
                    and (bool(re.match("^#[a-zA-Z0-9]{6}$", p[field_list_wo_cid[3]])) == True)
                    and ((p[field_list_wo_cid[4]][:-2].isdigit() == True and 150 <= int(p[field_list_wo_cid[4]][:-2]) <= 193 and p[field_list_wo_cid[4]][-2:]=='cm') 
                        or 
                        (p[field_list_wo_cid[4]][:-2].isdigit() == True and 59 <= int(p[field_list_wo_cid[4]][:-2]) <= 76 and p[field_list_wo_cid[4]][-2:]=='in'))
                    and (p[field_list_wo_cid[5]].isdigit() and len(p[field_list_wo_cid[5]])==4 and 2010 <= int(p[field_list_wo_cid[5]]) <= 2020)
                    and (bool(re.match("^[0-9]{9}$", p[field_list_wo_cid[6]])) == True)
                    )]
           
print('Number of valid passport:',len(valid_passport))
