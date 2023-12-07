import random

def gen_react_num(lower, upper):
    num = str(round(random.uniform(lower, upper),3))
    if len(num) <3:
        num.rjust(3, "0")
    num = num + "E+00"
    return num

def gener_react(reacts_theo, reacts_unpr):
    changes_arr = [[], []]
    for i, arr in enumerate([reacts_theo, reacts_unpr]):
        if i == 0:
            for el in arr:
                changes_arr[0].append(gen_react_num(0.5, 1.5))
        if i == 1:
            for el in arr:
                changes_arr[1].append(gen_react_num(0.8, 1.2))
    reacts = reacts_theo + reacts_unpr
    changes = changes_arr[0] + changes_arr[1]
    return reacts, changes

def save_react_chang(iter_num, location, reacts, changes):
    with open(location, "a") as f:
        f.write(f"{iter_num}\n{reacts}\n{changes}\n")
