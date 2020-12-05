import re

with open('input', 'r') as _input:
    passport_data = _input.read()

# Passport in the input data are visually separated by blank lines
# Split the data according to that rule and store into a list
passports_separated = re.split("[\n]+[\n]+", passport_data)

# list of passport with key:value pairs
passport_list = []

for p in passports_separated:  
    passport = dict()
    item = re.split('[\n ]+', p)
    for pair in item:
        passport[pair.split(':')[0]] = pair.split(':')[1]
    passport_list+=[passport]

f = sorted(['byr','iyr','eyr','hgt','hcl','ecl','pid'])  # --> sorted field list

valid_passport_list = []

for p in passport_list:
    sorted_key = sorted(p.keys())
    if 'cid' in sorted_key:
        sorted_key.remove('cid')
    check = all(item in sorted_key for item in f)
    if check == True:
        valid_passport_list.append(p)

#* sorted key list: ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
valid_passport = [p for p in valid_passport_list if (
                        (p[f[0]].isdigit() and len(p[f[0]])==4 and 1920 <= int(p[f[0]]) <= 2002)
                    and (p[f[1]] in ['amb','blu','brn','gry','grn','hzl','oth'])
                    and (p[f[2]].isdigit() and len(p[f[2]])==4 and 2020 <= int(p[f[2]]) <= 2030)
                    and (bool(re.match("^#[a-zA-Z0-9]{6}$", p[f[3]])) == True)
                    and ((p[f[4]][:-2].isdigit() and 150 <= int(p[f[4]][:-2]) <= 193 and p[f[4]][-2:]=='cm') 
                        or 
                        (p[f[4]][:-2].isdigit() and 59 <= int(p[f[4]][:-2]) <= 76 and p[f[4]][-2:]=='in'))
                    and (p[f[5]].isdigit() and len(p[f[5]])==4 and 2010 <= int(p[f[5]]) <= 2020)
                    and (bool(re.match("^[0-9]{9}$", p[f[6]])) == True)
                    )]

print('Part 2: Number of valid passport:',len(valid_passport))
