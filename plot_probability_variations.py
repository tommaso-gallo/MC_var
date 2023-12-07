from matplotlib import pyplot as plt
import numpy as np


# given the lines of savemassf and the element name, it extracts the abundances throughout all the runs
def get_element_abundances(lines, el_name):
    header = lines[0]
    ind = header.find(el_name)
    beg_ind = header.rfind("|", 0, ind)
    end_ind = header.find("|", ind)
    abundances = []
    for line in lines[1:]:  # line 0 is the header
        abundances.append(float(line[beg_ind + 1:end_ind].replace(" ", "").replace("E", "e")))
    return abundances


# given the lines of save_massf extracts the abundances of all the elements
def get_all_abundances(lines):
    header = lines[0]
    indices = [i for i, l in enumerate(header) if l == "|"]
    all_abundances = []
    isotope_names = []
    isotope_nums = []
    for ind in indices[:-1]:  # since the header terminates with "|" and no element after it
        element_name = header[ind + 6:ind + 11]
        isotope_names.append(element_name[:2])
        isotope_nums.append(element_name[2:])
        all_abundances.append(get_element_abundances(lines, element_name))
    # print(isotope_names, isotope_nums)
    return all_abundances, isotope_names, isotope_nums


# given the iterable of iterables which contain the final abundances for each element for each run, gives the same
# values back but as (abundance-mean)/mean
def get_all_variations(all_abundances):
    mean_vars = []  # the mean variation
    all_variations = []
    for abundances in all_abundances:
        variations = []
        mean = np.mean(abundances)
        for abund in abundances:
            variations.append((abund - mean) / mean)
        mean_vars.append(np.mean(variations))
        all_variations.append(variations)
    return all_variations


# variations are as described above, the delims are ranges to which the variations are cut-off e.g. if the
# variations for an element are (-2, 0, 1, 3, 5) then delims[1]=1 transforms this to (0, 1, 3), i.e. the 60% percentile
# names are the names of the element of which each iterable in variations refers to (e.g. GA, GE, PB...) and nums are
# the mass numbers of each iterable in variations
def plot_variations(all_variations, delims, names, nums, cutoff):
    fig, ax = plt.subplots()
    counter = 0
    ind_isot_2_delete = []
    for l, variation in enumerate(all_variations):
        new_var = np.sort(np.copy(variation))
        if abs(new_var[0]) > cutoff or abs(new_var[-1]) > cutoff:
            for i, lim in enumerate(delims):
                cut_new_var = new_var[lim:-lim]
                if lim == 0:
                    cut_new_var = new_var
                base = float(cut_new_var[0])
                top = float(cut_new_var[-1])
                height = top - base
                plt.bar([counter], [height], bottom=base, color=(0, 0, 1, 0.1 + (i) / len(delims)))
            counter += 1
        else:
            ind_isot_2_delete.append(l)
    new_nums = np.delete(nums, ind_isot_2_delete)
    new_names = np.delete(names, ind_isot_2_delete)
    ax_t = ax.secondary_xaxis("top")
    ax_t.set_xticks([i for i in range(0, len(new_nums), 2)], [new_nums[i] for i in range(0, len(new_nums), 2)], minor=False)
    ax_t.set_xticks([i for i in range(1, len(new_nums), 2)], [new_nums[i] for i in range(1, len(new_nums), 2)], minor=True)
    ax_t.tick_params("x", which="minor", direction="in", pad=-15)
    ax.set_xticks([i for i in range(0, len(new_names), 2)], [new_names[i] for i in range(0, len(new_names), 2)], minor=False)
    ax.set_xticks([i for i in range(1, len(new_names), 2)], [new_names[i] for i in range(1, len(new_names), 2)], minor=True)
    ax.tick_params("x", which="minor", direction="in", pad=-15)
    plt.show()


# puts all the functions defined previously together. The final plot has on the x axis the isotopes and on the y axis
# the relative variations divided in percentile as described above, set by delims and showed as different opacities of
# the same color. The isotopes are nicely labeled with their parent element name (e.g. PB for PB206) on the bottom of
# the image and the mass number on the top
def generate_plot(xtime_save_path, delims):
    with open(xtime_save_path, "r") as f:
        lines = f.readlines()
    all_abundances, names, nums = get_all_abundances(lines)
    all_variations = get_all_variations(all_abundances)
    plot_variations(all_variations, delims, names, nums, cutoff=0.175)

delims = [0, 1]
generate_plot("C:/Users\pc\Desktop\programmazione\programmi/battino\MC-var/save_massf_best.txt", delims)
