# str[start:stop:step]

trial = 'biggie'
#new_trial = trial[::-1]

# print(new_trial)


def reverse_string(str):
    if len(str) == 0:
        return str
    else:
        return reverse_string(str[1:]) + str[0]


print("Recursive fn: ", reverse_string(trial))
