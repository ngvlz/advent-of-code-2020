import list_of_passwords

correct_password = list()

input_passwd = list_of_passwords.get_input()

lines_of_passwd = input_passwd.split('\n')

for line in lines_of_passwd:
    passwd = line.split(': ', 1)[1]
    
    passwd_policy = line.split(': ', 1)[0]
    policy_range = passwd_policy.split(' ')[0]
    min_range = int(policy_range.split('-')[0])
    max_range = int(policy_range.split('-')[1]) + 1
    letter_to_check = passwd_policy.split(' ')[1]
    
    if passwd.count(letter_to_check) in range(min_range, max_range):
        correct_password.append(passwd)
    else:
        pass

print(len(correct_password))