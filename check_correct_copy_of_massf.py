def check_correct_copy(orig_path, copy_path):
    correct = True
    with open(copy_path, "r") as f:
        lines = f.readlines()
        header = lines[0]
        last_line = lines[-1]
        tick_indices = [i for i, l in enumerate(header) if l == "-"]
        elements_copy = [header[ind + 1:ind + 6] for ind in tick_indices]
        quantities_copy = [last_line[ind - 3:ind + 8] for ind in tick_indices]
    with open(orig_path, "r") as g:
        lines = g.readlines()
        header = lines[0]
        last_line = lines[-1]
        indices = [header.index(elem) for elem in elements_copy]
        quantities_orig = [last_line[ind - 4:ind + 7] for ind in indices]
    #        print(quantities_orig, quantities_copy)
    for i, copy_quant in enumerate(quantities_copy):
        if copy_quant != quantities_orig[i]:
            correct = False
            print(f'wrong quantity found in copying of xtime: {quantities_orig[i]} orig vs {copy_quant}')
    return correct


# xtime_path = "C:/Users/pc/Desktop/programmazione/programmi/battino/xtimes/x-time_old.txt"
# print(check_correct_copy(xtime_path, "save_massf.txt"))
"""

def get_element(line0, lastline, el_name):
    header = str(line0)
    ind = header.find(el_name)
    beg_ind = header.rfind("|", 0, ind)
    end_ind = header.find("|", ind)
    print(lastline[beg_ind + 1:end_ind])


def check_correct_copy(orig_path, copy_path):
    with open(orig_path, "r") as f:
        lines = f.readlines()
        line0_1 = lines[0]
        lastline_1 = lines[-1]

    with open(copy_path, "r") as g:
        lines = g.readlines()
        line0_2 = lines[0]
        lastline_2 = lines[-1]

    correct = True
    for i in range(5):
        start_search = 8400 + 5000 * i
        ind_1 = lastline_1.index("E-0", start_search)
        beg_ind_1 = lastline_1.rfind("-", 0, ind_1) + 3
        end_ind_1 = lastline_1.find("-", ind_1) + 3
        element_long = line0_1[beg_ind_1:end_ind_1]
        # print(element_long, beg_ind_1, end_ind_1)
        element = element_long[element_long.index("-"):element_long.index("-") + 6]
        massf_1 = lastline_1[beg_ind_1:end_ind_1]
        ind_2 = line0_2.find(element)
        beg_ind_2 = lastline_2.rfind("-", 0, ind_2) + 3
        end_ind_2 = lastline_2.find("-", ind_2) + 3
        massf_2 = lastline_2[beg_ind_2:end_ind_2]
        print(massf_1, massf_2)
        if massf_1 != massf_2:
            correct = False
            break
    return correct
"""
