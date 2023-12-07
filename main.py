# import relevant modules
import subprocess
import os

from copy_else_dir import create_folder
from create_reacts import gener_react, save_react_chang
from create_netset import write_netset

from extract_data import create_save_massf, save_data
from check_correct_copy_of_massf import check_correct_copy

# number of the line of the reactions varied
reacts_theo = [4825, 4826]  # reaction with ony theoretical prediction
reacts_unpr = [4828, 4829, 4830]  # reactions with low precision

# nuclides to be studied
isotopes = ['GA 69', 'GA 71', 'GE 70', 'GE 72', 'GE 74', 'AS 75', 'SE 76', 'SE 78', 'SE 80', 'BR 79', 'BR 81', 'KR 80',
            'KR 82', 'KR 84', 'KR 86', 'RB 85', 'RB 87', 'SR 86', 'SR 87', 'SR 88', 'Y  89', 'ZR 90', 'ZR 92', 'ZR 94',
            'NB 93', 'MO 95', 'MO 96', 'MO 97', 'MO 98', 'RU 99', 'RU100', 'RU102', 'RH104', 'PD104', 'PD106', 'PD108',
            'AG107', 'AG109', 'CD110', 'CD112', 'CD114', 'IN115', 'SN116', 'SN118', 'SN120', 'SB121', 'TE122', 'TE123',
            'TE124', 'TE126', 'I 127', 'XE128', 'XE130', 'XE132', 'CS133', 'BA134', 'BA136', 'BA137', 'BA138', 'LA139',
            'CE140', 'PR141', 'ND142', 'ND144', 'ND146', 'SM147', 'SM148', 'SM150', 'EU151', 'EU153', 'GD152', 'GD154',
            'GD156', 'GD158', 'TB159', 'DY160', 'DY162', 'DY164', 'HO165', 'ER166', 'ER167', 'ER168', 'TM169', 'YB170',
            'YB172', 'YB174', 'LU175', 'LU176', 'HF176', 'HF178', 'HF180', 'TA181', 'W 182', 'W 183', 'W 184', 'RE185',
            'OS186', 'OS187', 'OS188', 'OS190', 'IR191', 'IR193', 'PT192', 'PT194', 'PT196', 'AU197', 'HG198', 'HG200',
            'HG202', 'TL203', 'TL205', 'PB204', 'PB206', 'PB207', 'PB208', 'BI209']

dir_template_path = "prova_template/"  # the directory of the folder containing all the necessary files
dir_target_root = "C:/Users/pc/Desktop/programmazione/programmi/battino/MC-var/"  # directory in which the run will be created
dir_target_name = "run_"  # name of the run directory (the number of the run will be added for each run)

orig_netset = "networksetup.txt"  # directory of the original networksetup that will be used as a copy
new_netset = "new_netset.txt"  # name of the new networksetup
change_reacts_save = "input_reacts.txt"  # path to the file that will contain the rates of the reactions changed in each run

ppn_path = ""  # path to ppn.exe

path_save_massf = "save_massf.txt"  # path to the file to whici the massfractions are calculated
xtime_filename = "x-time.txt"  # name of the xtime file

# the main loop
for run_num in range(2):
    run_dir = dir_target_root + dir_target_name + str(run_num)  # directory of each run
    create_folder(dir_template_path, dir_target_root, dir_target_name + str(run_num))  # create a new run
    reacts, changes = gener_react(reacts_theo, reacts_unpr)  # generate random rates of reaction
    write_netset(reacts, changes, orig_netset,
                 run_dir + "/" + new_netset)  # write a new networksetup in the run created
    save_react_chang(run_num, change_reacts_save, reacts, changes)  # save the reactions that have been changed
    os.chdir(run_dir)  # change the working directory to that of the run
    subprocess.run([ppn_path])  # run ppn
    if run_num == 0:
        indices = create_save_massf(xtime_path=run_dir + "/" + xtime_filename, save_massf_path=path_save_massf, nuclides=isotopes)
        # create the file to which the final massfraction are copied
    save_data(xtime_path=run_dir + "/" + xtime_filename, save_massf_path=path_save_massf, indices=indices, run_num=run_num)
    # save the final massfs
    correc_copy_massf = check_correct_copy(orig_path=run_dir + "/" + xtime_filename,
                                           copy_path=path_save_massf)  # check that the massf was copied correctly
    if not correc_copy_massf:
        print(f"!!!!! An error occured in copying the final massfraction of the {run_num}th run !!!!!")

"""
['FE 58', 'CO 59', 'NI 58', 'NI 60', 'NI 61', 'NI 62', 'NI 64', 'CU 63', 'CU 65', 'ZN 64', 'ZN 66', 'ZN 67', 'ZN 68', 
 'ZN 70', 'GA 69', 'GA 71', 'GE 70', 'GE 72', 'GE 73', 'GE 74', 'GE 76', 'AS 75', 'SE 74', 'SE 76', 'SE 77', 'SE 78', 
 'SE 80', 'SE 82', 'BR 79', 'BR 81', 'KR 78', 'KR 80', 'KR 82', 'KR 83', 'KR 84', 'KR 86', 'RB 85', 'RB 87', 'SR 84', 
 'SR 86', 'SR 87', 'SR 88', 'Y  89', 'ZR 90', 'ZR 91', 'ZR 92', 'ZR 94', 'ZR 96', 'NB 93', 'MO 92', 'MO 94', 'MO 95', 
 'MO 96', 'MO 97', 'MO 98', 'MO100', 'RU 96', 'RU 98', 'RU 99', 'RU100', 'RU101', 'RU102', 'RU104', 'RH103', 
 'PD102', 'PD104', 'PD105', 'PD106', 'PD108', 'PD110', 'AG107', 'AG109', 'CD106', 'CD108', 'CD110', 'CD111', 'CD112', 
 'CD113', 'CD114', 'CD116', 'IN113', 'IN115', 'SN112', 'SN114', 'SN115', 'SN116', 'SN117', 'SN118', 'SN119', 'SN120', 
 'SN122', 'SN124', 'SB121', 'SB123', 'TE120', 'TE122', 'TE123', 'TE124', 'TE125', 'TE126', 'TE128', 'TE130', 'I 127', 
 'XE124', 'XE126', 'XE128', 'XE129', 'XE130', 'XE131', 'XE132', 'XE134', 'XE136', 'CS133', 'BA130', 'BA132', 'BA134', 
 'BA135', 'BA136', 'BA137', 'BA138', 'LA139', 'CE136', 'CE138', 'CE140', 'CE142', 'PR141', 'ND142', 'ND143', 'ND144', 
 'ND145', 'ND146', 'ND148', 'ND150', 'SM144', 'SM148', 'SM149', 'SM150', 'SM152', 'SM154', 'EU151', 'EU153', 'GD152', 
 'GD154', 'GD155', 'GD156', 'GD157', 'GD158', 'GD160', 'TB159', 'DY156', 'DY158', 'DY160', 'DY161', 'DY162', 'DY163', 
 'DY164', 'HO165', 'ER162', 'ER164', 'ER166', 'ER167', 'ER168', 'ER170', 'TM169', 'YB168', 'YB170', 'YB171', 'YB172', 
 'YB173', 'YB174', 'YB176', 'LU175', 'HF174', 'HF176', 'HF177', 'HF178', 'HF179', 'HF180', 'TA181', 'W 180', 'W 182', 
 'W 183', 'W 184', 'W 186', 'RE185', 'OS186', 'OS187', 'OS188', 'OS189', 'OS190', 'OS192', 'IR191', 'IR193', 'PT192', 
 'PT194', 'PT195', 'PT196', 'PT198', 'AU197', 'HG196', 'HG198', 'HG199', 'HG200', 'HG201', 'HG202', 'HG204', 'TL203', 
 'TL205', 'PB204', 'PB206', 'PB207', 'PB208', 'BI209']
 
    if i == 0:
        beg_ind, end_ind = create_save_massf(run_dir + "/" + xtime_filename,
                                             path_save_massf)  # create the file to which the final massfraction are copied
        # beg_ind and end_ind are the indices between which every element from FE 59 and BI 209 are contained
    save_data(run_dir + "/" + xtime_filename, path_save_massf, beg_ind, end_ind, i)  # save the final massfs
    correc_copy_massf = check_correct_copy(run_dir + "/" + xtime_filename,
                                           path_save_massf)  # check that the massf was copied correctly
    if not correc_copy_massf:
        print(f"an error occured in copying the final massfraction of the {i}th run")
 

things to check:
- all variations where extracted (in plot probability variations, length of variations = number of runs)
"""