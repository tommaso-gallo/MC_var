def write_netset(reacts, changes, orig_file, new_file):
    with open(new_file, "w") as f:
        with open(orig_file, "r") as g:
            for i, line in enumerate(g.readlines(), 1):
                if i in reacts:
                    f.writelines(line.replace("1.000E+00", changes[reacts.index(i)]))
                else:
                    f.writelines(line)