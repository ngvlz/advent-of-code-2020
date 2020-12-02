import list_of_passwords

correct_password = list()

input_passwd = list_of_passwords.get_input()

lines_of_passwd = input_passwd.split('\n')

for line in lines_of_passwd:
    passwd = line.split(': ', 1)[1]

    passwd_policy = line.split(': ', 1)[0]
    get_position_from_policy = passwd_policy.split(' ')[0].split('-')
    position_converted_to_int = list(map(int, get_position_from_policy))
    letter_to_check = passwd_policy.split(' ')[1]

    count = 0
    for idx, char in enumerate(passwd):
        pos = idx + 1
        if char == letter_to_check and pos in position_converted_to_int:
            count += 1
        else:
            pass   

    if count == 2:
        pass
    elif count == 1:
        correct_password.append(passwd)
    else:
        pass

print(len(correct_password))