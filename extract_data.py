def create_save_massf(xtime_path, save_massf_path, nuclides):
    header = "# run        |"
    with open(xtime_path, "r") as g:
        line0 = g.readline()
        all_indices = [i for i, l in enumerate(line0) if l == "|" and 56 < i < len(line0) - 9]
        long_els = [line0[i + 1:i + 14] for i in all_indices]
        el_names = [long_el[5:10] for long_el in long_els]
    indices = []
    for nuclide in nuclides:
        header += long_els[el_names.index(nuclide)]
        indices.append(all_indices[el_names.index(nuclide)])
    #print(header)
    with open(save_massf_path, "w") as f:
        f.write(header + "\n")
        print("save_massf created")
    return indices

def save_data(xtime_path, save_massf_path, indices, run_num):
    massfs = str(run_num).ljust(12, " ") + "|"
    with open(xtime_path, "r") as f:
        lines = f.readlines()
        last_line = lines[-1]
        for ind in indices:
            massfs += last_line[ind:ind+13]
    with open(save_massf_path, "a") as g:
        g.write(massfs + "\n")



xtime_path = "C:/Users/pc/Desktop/programmazione/programmi/battino/xtimes/x-time_old.txt"
nuclides = ['FE 58', 'CO 59', 'NI 58', 'NI 60', 'NI 61', 'NI 62', 'NI 64', 'CU 63', 'CU 65', 'ZN 64', 'ZN 66', 'ZN 67',
            'ZN 68', 'ZN 70', 'GA 69', 'GA 71', 'GE 70', 'GE 72', 'GE 73', 'GE 74', 'GE 76', 'AS 75', 'SE 74', 'SE 76',
            'SE 77', 'SE 78', 'SE 80', 'SE 82', 'BR 79', 'BR 81', 'KR 78', 'KR 80', 'KR 82', 'KR 83', 'KR 84', 'KR 86',
            'RB 85', 'RB 87', 'SR 84', 'SR 86', 'SR 87', 'SR 88', 'Y  89', 'ZR 90', 'ZR 91', 'ZR 92', 'ZR 94', 'ZR 96',
            'NB 93', 'MO 92', 'MO 94', 'MO 95', 'MO 96', 'MO 97', 'MO 98', 'MO100', 'RU 96', 'RU 98', 'RU 99', 'RU100',
            'RU101', 'RU102', 'RU104', 'RH103', 'PD102', 'PD104', 'PD105', 'PD106', 'PD108', 'PD110', 'AG107', 'AG109',
            'CD106', 'CD108', 'CD110', 'CD111', 'CD112', 'CD113', 'CD114', 'CD116', 'IN113', 'IN115', 'SN112', 'SN114',
            'SN115', 'SN116', 'SN117', 'SN118', 'SN119', 'SN120', 'SN122', 'SN124', 'SB121', 'SB123', 'TE120', 'TE122',
            'TE123', 'TE124', 'TE125', 'TE126', 'TE128', 'TE130', 'I 127', 'XE124', 'XE126', 'XE128', 'XE129', 'XE130',
            'XE131', 'XE132', 'XE134', 'XE136', 'CS133', 'BA130', 'BA132', 'BA134', 'BA135', 'BA136', 'BA137', 'BA138',
            'LA139', 'CE136', 'CE138', 'CE140', 'CE142', 'PR141', 'ND142', 'ND143', 'ND144', 'ND145', 'ND146', 'ND148',
            'ND150', 'SM144', 'SM148', 'SM149', 'SM150', 'SM152', 'SM154', 'EU151', 'EU153', 'GD152', 'GD154', 'GD155',
            'GD156', 'GD157', 'GD158', 'GD160', 'TB159', 'DY156', 'DY158', 'DY160', 'DY161', 'DY162', 'DY163', 'DY164',
            'HO165', 'ER162', 'ER164', 'ER166', 'ER167', 'ER168', 'ER170', 'TM169', 'YB168', 'YB170', 'YB171', 'YB172',
            'YB173', 'YB174', 'YB176', 'LU175', 'HF174', 'HF176', 'HF177', 'HF178', 'HF179', 'HF180', 'TA181', 'W 180',
            'W 182', 'W 183', 'W 184', 'W 186', 'RE185', 'OS186', 'OS187', 'OS188', 'OS189', 'OS190', 'OS192', 'IR191',
            'IR193', 'PT192', 'PT194', 'PT195', 'PT196', 'PT198', 'AU197', 'HG196', 'HG198', 'HG199', 'HG200', 'HG201',
            'HG202', 'HG204', 'TL203', 'TL205', 'PB204', 'PB206', 'PB207', 'PB208', 'BI209']

"""
# wrong because it used the order of nuclides in xtime path (which had for example PB206, 207 in position 53 and 54)
def create_save_massf(xtime_path, save_massf_path, nuclides):
    header = "# run       |"
    with open(xtime_path, "r") as g:
        line0 = g.readline()
        long_els = [line0[i + 1:i + 14] for i, l in enumerate(line0) if l == "|" and 56 < i < len(line0) - 9]
    positions = []
    for long_el in long_els:
        print(long_el)
        ind = long_el.index("-")
        el_name = long_el[ind + 1:ind + 6]
        if el_name in nuclides:
            positions.append(line0.index(long_el))
            header = header + long_el
    with open(save_massf_path, "w") as f:
        f.write(header + "\n")
        print("save_massf created")
    return positions

def save_data(xtime_path, save_massf_path, indices, run_num):
    with open(xtime_path, "r") as f:
        lines = f.readlines()
        last_line = lines[-1]
        massfs = str(run_num).ljust(13, " ")
        for ind in indices:
            massfs = massfs + (last_line[ind:ind + 13])
    with open(save_massf_path, "a") as g:
        g.write(massfs)

#__________________________________________________________
def create_save_massf(xtime_path, save_massf_path):
    with open(xtime_path, "r") as g:
        line = g.readline()
        beg_ind = line.index("| 643-FE 59  |")
        end_ind = line.index("|4750-BI209  |") + len("|4750-BI209  |")
    header = "# run   " + line[beg_ind:end_ind]
    with open(save_massf_path, "w") as f:
        f.write(header + "\n")
        print("save_massf created")
    return beg_ind, end_ind


def save_data(xtime_path, save_massf_path, beg_ind, end_ind, run_num):
    with open(xtime_path, "r") as g:
        line = g.readlines()[-1]
    massf = str(run_num).rjust(8, " ") + line[beg_ind:end_ind] + "\n"
    with open(save_massf_path, "a") as f:
        f.write(massf)
        print(f"massf for {run_num} saved")
"""
