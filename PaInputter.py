# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:10:05 2022

@author: seblom
"""

import pandas as pd
import numpy as np
from psychopy.tools.filetools import fromFile
import sys
import time

try:
    cond_data = pd.read_csv('conditioning_data.csv',index_col=0)
    backup = pd.read_csv('conditioning_data.csv')
    print("""
-------------------------------------
| Existing data found! Data loaded. |
-------------------------------------
    """)
    time.sleep(1)
except:
    cond_data = pd.DataFrame()
    print("""
-----------------------------------
| No existing data. Data created! |
-----------------------------------
    """)
    time.sleep(1)
print("""
This program is used to add a column of pain estimations to an experiment file from PsychoPy.
The program will then append the registered data into a file called "conditioning_data.csv".
""")
time.sleep(0.5)

data_input = input('Enter the participant ID here: ')
färdig = 0
check_int = 0
check_v1 = 0
check_v2 = 0
check_file = 0
folder =        'data/'
extring_v1_1 =  '_cond_learning.psydat'
extring_v1_2 =  '_cond_second.psydat'
extring_v1_3 =  '_cond_trial.psydat'
extring_v2 =    "_cond_revised.psydat"
while not färdig:
    try:
        check_int = isinstance(int(data_input),int)
        psydata_v2 = fromFile(folder+data_input+extring_v2)
        df_all = pd.DataFrame(data = psydata_v2.entries)
        check_v2 = isinstance(df_all, pd.DataFrame)
    except:
        print()
    try:
        check_int = isinstance(int(data_input),int)
        psydata_v1 = fromFile(folder+data_input+extring_v1_1)
        df_1 = pd.DataFrame(data = psydata_v1.entries)
        check_v1 = isinstance(df_1, pd.DataFrame)
    except:
        print()
    check_file = check_v1 | check_v2
    if check_int == 1 and check_file==1:
        färdig = True
    else:
        print('''Invalid input! Please try again.
              ''')
        time.sleep(0.5)
        data_input = input('Enter the participant ID here: ')

if check_v2 == True:

    psydata = fromFile(folder+data_input+extring_v2)
    df_all = pd.DataFrame(data = psydata.entries)
    df_all = df_all.sort_index(axis=1)

if check_v1 == True:
    psydata_1 = fromFile(folder+data_input+extring_v1_1)
    psydata_2 = fromFile(folder+data_input+extring_v1_2)
    psydata_3 = fromFile(folder+data_input+extring_v1_3)
    df_1 = pd.DataFrame(data = psydata_1.entries)
    df_1 = df_1.sort_index(axis=1)
    df_2 = pd.DataFrame(data = psydata_2.entries)
    df_2 = df_2.sort_index(axis=1)
    df_3 = pd.DataFrame(data = psydata_3.entries)
    df_3 = df_3.sort_index(axis=1)
    frames = [df_1, df_2, df_3]
    df_all = pd.concat(frames, ignore_index=True)

print("""
--------------------------
| EXTRACTION SUCCESSFUL! |
--------------------------
""")
time.sleep(0.5)
print('''
  Time to add the pain estimations (VAS) from the experiment into the Data Frame.
  Remember: If you have put in an incorrect pain estimation, you can always
  revert by entering a negative number (Example: -5).

  To see a list of available commands, enter "c".
      ''')
time.sleep(0.5)
row, col = df_all.shape
painput_all = np.zeros((row))
i= 0
while i < row:
    painput = input('Pain estimation #' + str(i + 1) + ': ')
    time.sleep(0.1)
    färdig = 0
    check = 0
    while not färdig:
        try:
            check = isinstance(int(painput),int)
        except ValueError:
            if str(painput) == 'l':
                time.sleep(0.2)
                print('''
------------------------------------
| LISTING CURRENT PAIN ESTIMATIONS |
------------------------------------''')
                time.sleep(1)
                print('''

 _\t\t___\t\t  _
 |\tIDX\t |\tPAIN\t  |
 |-\t\t-|-\t\t -|''')
                for pain in range(i):
                    time.sleep(0.05)
                    print(''' |\t '''+str(pain+1)+'\t |\t '+str(painput_all[pain])[:-2]+'\t  |')
                print(' |-\t----\t-|-\t----\t -|')
                print()
            elif str(painput) =='q':
                print ('''
-------------------------
| QUIT COMMAND DETECTED |
-------------------------''')
                time.sleep(0.5)
                quitput = input('''
    Are you sure you want to quit?
    No progress will be saved!

    Enter "y" or "q" to quit.
    Enter anything else to continue.

-->''')
                if quitput == 'q':
                    sys.exit()
                elif quitput =='y':
                    sys.exit()
            elif str(painput) =='r':
                print('''
----------------------------
| Remaining Estimations: '''+str(row-i) +''' |
----------------------------
''')
                time.sleep(0.5)
            elif str(painput) == 'c':
                print('''
----------------------
| AVAILABLE COMMANDS |
----------------------

  -1/-2/...     - Go back to change the previous pain estimation

    c           - List of available commands

    e           - Edit a specific pain estimation

    l           - Listing the current pain estimations

    q           - Quit the program. No progress will be saved.

    r           - Tell the remaining amount pain estimates.

******************************************************************
''')
                time.sleep(0.5)


            elif str(painput) =='e':
                print('''
*************************************************************

-------------------------
| ENTERING EDITING MODE |
-------------------------
''')
                time.sleep(1)
                print('''
Below you can find the current list of pain estimates:

 _\t\t___\t\t  _
 |\tIDX\t |\tPAIN\t  |
 |-\t\t-|-\t\t -|''')
                for pain in range(i):
                    time.sleep(0.05)
                    print(''' |\t '''+str(pain+1)+'\t |\t '+str(painput_all[pain])[:-2]+'\t  |')
                print(' |-\t----\t-|-\t----\t -|')
                time.sleep(0.2)
                edit_index = input('''
*************************************************************

Please input the index that you would like to change below.
(Note: To exit Edit mode, simply enter any non-number)

--> ''')
                try:
                    edit_check = isinstance(int(edit_index),int)

                    if int(edit_check) == 1:
                        if int(edit_index)>0:
                            if int(edit_index)<int(i)+1:
                                time.sleep(0.5)
                                print('''
Index ''' +str(edit_index) +''' has been selected.
This index currently has the pain value ''' +str(painput_all[int(edit_index)-1]) +'''.''')
                                time.sleep(1)
                                edit_value = input('''
What would you like to change the value to?
(Note: To exit Edit mode, simply press any non-number)
--> ''')
                                try:
                                    edit_check = isinstance(int(edit_index),int)
                                    if int(edit_check) == 1:
                                        if int(edit_value)>0:
                                            painput_all[int(edit_index)-1] = edit_value
                                            print('''
********************************************
------------
| SUCCESS! |
------------
''')
                                            time.sleep(0.5)
                                            print('''
Index ''' + str(edit_index) +''' now has a pain rating of ''' + str(edit_value))
                                            time.sleep(0.5)
                                            print('''

------------------------
| EXITING EDITING MODE |
------------------------

''')
                                            time.sleep(0.5)

                                        else:
                                            print('''
---------------------------------------------
| NO NEGATIVE NUMBERS! EXITING EDITING MODE |
---------------------------------------------''')
                                            time.sleep(0.5)
                                    else:
                                        print('''
------------------------
| EXITING EDITING MODE |
------------------------

''')
                                        time.sleep(0.5)
                                except:
                                    print('''
------------------------
| EXITING EDITING MODE |
------------------------

''')
                                    time.sleep(0.5)

                            else:
                                print('''
----------------------------------------------------
| INDEX OUT OF CURRENT RANGE. EXITING EDITING MODE |
----------------------------------------------------
''')
                                time.sleep(0.5)
                        else:
                            print('''
----------------------------------------------
| NO IDX AT 0 OR BELOW. EXITING EDITING MODE |
----------------------------------------------
''')
                            time.sleep(0.5)

                except:
                    print('''
------------------------
| EXITING EDITING MODE |
------------------------

''')
                    time.sleep(0.5)




            else:
                print('''
Invalid input! Please try again.
Tip: Enter "c" to see available commands.''')
                time.sleep(0.2)




        if check == 1:
            if int(painput)<0:
                i -=1
                print('''
---------------------------
| REVERT COMMAND DETECTED |
---------------------------
''')
                time.sleep(0.5)
                print('''
    You have now reverted to Pain estimation number ''' + str(i+1) +'''.
    Previous pain input here was: ''' + str(painput_all[i]) + '''.

    Please enter below what you would like to change the VAS to.
    Remember, you can revert again if you want to back further.
''')

                färdig = True
            else:
                painput_all[i] = int(painput)
                i +=1
                färdig = True

        else:
            painput = input('Pain estimation #' + str(i + 1) + ': ')
    print()

print('''
--------------------------------------
| '''+str(i)+''' ESTIMATIONS SUCCESSFULLY ADDED! |
--------------------------------------

''')
time.sleep(0.5)

färdig = 0
while not färdig:
    print('''Below you can find the current list of pain estimates:


 _\t\t___\t\t  _
 |\tIDX\t |\tPAIN\t  |
 |-\t\t-|-\t\t -|''')
    for pain in range(len(painput_all)):
        time.sleep(0.05)
        print(''' |\t '''+str(int(pain)+1)+'\t |\t '+str(painput_all[pain])[:-2]+'\t  |')
    print(' |-\t----\t-|-\t----\t -|')

    save = input('''
To save the current data, enter "s".
If any other key is entered, you will enter editing mode.

-->''')
    if str(save) =='s':
        färdig = True
    else:
        print('''
*************************************************************

-------------------------
| ENTERING EDITING MODE |
-------------------------''')
        time.sleep(1)
        print('''

Below you can find the current list of pain estimates:
 _\t\t___\t\t  _
 |\tIDX\t |\tPAIN\t  |
 |-\t\t-|-\t\t -|''')
        for pain in range(i):
            time.sleep(0.05)
            print(''' |\t '''+str(pain+1)+'\t |\t '+str(painput_all[pain])[:-2]+'\t  |')
        print(' |-\t----\t-|-\t----\t -|')
        time.sleep(0.2)
        edit_index = input('''
*************************************************************

Please input the index that you would like to change below.
(Note: To exit Edit mode, simply enter any non-number)

--> ''')
        try:
            edit_check = isinstance(int(edit_index),int)

            if int(edit_check) == 1:
                if int(edit_index)>0:
                    print('''
***************************************************

Index ''' +str(edit_index) +''' has been selected.
This index currently has the pain value ''' +str(painput_all[int(edit_index)-1]) +'''.''')
                    time.sleep(1)
                    edit_value = input('''
What would you like to change the value to?
(Note: To exit Edit mode, simply press any non-number)
--> ''')
                else:
                    print('''
----------------------------------------------
| NO IDX AT 0 OR BELOW. EXITING EDITING MODE |
----------------------------------------------
''')
                    time.sleep(0.5)
            try:
                edit_check = isinstance(int(edit_index),int)
                if int(edit_check) == 1:
                    if int(edit_value)>0:
                        painput_all[int(edit_index)-1] = edit_value
                        print('''
********************************************
------------
| SUCCESS! |
------------

Index ''' + str(edit_index) +''' now has a pain rating of''' + str(edit_value))
                        time.sleep(0.5)
                        print('''

------------------------
| EXITING EDITING MODE |
------------------------

''')
                        time.sleep(0.5)

                    else:
                        print('''
---------------------------------------------
| NO NEGATIVE NUMBERS! EXITING EDITING MODE |
---------------------------------------------''')
                        time.sleep(1)
                else:
                    print('''
------------------------
| EXITING EDITING MODE |
------------------------

''')
                    time.sleep(0.5)
            except:
                print('''
------------------------
| EXITING EDITING MODE |
------------------------

''')
                time.sleep(0.5)




        except:
            print('''
------------------------
| EXITING EDITING MODE |
------------------------

''')
            time.sleep(0.5)

df_all['VAS'] = painput_all

idxnr = np.zeros((row))
for i in range(0,row):
    idxnr[i] =i+1
df_all['idx'] = idxnr

d = pd.DataFrame({
    'stim_index':       df_all['idx'],
    'participant':      df_all['participant'],
    'temperature':      df_all['temperature'],
    'phase':            df_all['phase'],
    'image_left':       list(map(lambda x: x.split('.')[0],df_all['image_l'])),
    'image_right':      list(map(lambda x: x.split('.')[0],df_all['image_r'])),
    'stimulus':         df_all['CS'],
    'level_pain':       df_all['temp_stim'],
    'jitter':           df_all['jitter'],
    'pain':             df_all['VAS']
    })

cond_data = cond_data.append(d,ignore_index=True)
cond_data.to_csv('conditioning_data.csv')
time.sleep(0.2)
print('''
---------------------------
| DATA SUCCESSFULLY SAVED |
|                         |
|       THANK YOU!        |
|                         |
|    HAVE A NICE DAY!     |
---------------------------''')

time.sleep(1)
