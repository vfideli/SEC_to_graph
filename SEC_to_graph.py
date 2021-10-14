# -*- coding: utf-8 -*-
# Python 3.8
"""
Author:     Vincent Fideli
Created: Sat Oct  2 13:24:07 2021

Description
-----------
Imports .txt file from SEC AKTA, outputs a graph with legends, labelled axes, and title.

"""
import numpy as np
import matplotlib.pyplot as plt


### SEC curves

sec_file = input("File name? ")

# reads and decodes file to unicode
fread = open(sec_file, 'rb').read()
sec_txt = fread.decode('utf-16')

# removes first three lines (headers)
sec_txt_noheader = sec_txt.split("\n",3)[3]

# find out two columns to use
num_lines = sum(1 for line in sec_txt_noheader)
no_columns = np.arange(10)
while len(no_columns) > 2:
    for x in sec_txt_noheader.splitlines():
        for i in no_columns:
            if x.split('\t')[i] == "":
                no_columns = no_columns[no_columns != i]
                # print("removed ", i)
# print(no_columns)

# set up ml from sec_txt
ml = []
mAU = []
for x in sec_txt_noheader.splitlines():
    ml.append(float(x.split('\t')[no_columns[0]]))
    mAU.append(float(x.split('\t')[no_columns[1]]))

# Remove negatives
ml = np.array([x for x in ml if x >= 0])
mAU = np.array(mAU[len(mAU) - len(ml):])

# Graph SEC Abs vs ml from array to figure

plt.close()
title = input("Title? ")
plt.plot(ml, mAU, 'b')
plt.title(title)
plt.xlabel("Elution volume (ml)")
plt.ylabel("$A_{280}$ (mAU)")


# plt.tight_layout()




























