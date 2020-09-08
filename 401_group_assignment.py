# -*- coding: utf-8 -*-
"""

Generate project sets with minimal student overlap

"""
import itertools
import numpy as np
import random
import math

num_students = 50
group_size = 3
number_groups = 17
student_list = np.arange(0, num_students, 1)
student_list2 = np.append(student_list,100)

def getGroups(student_list, grouping1, grouping2,  number_students):
    proj_1 = list(grouper(3, range(num_students)))
    proj_1[-1] = [proj_1[-1][0], proj_1[-1][1], 100]
    found = 0
    
    while found == 0:
        proj_2 = partition(student_list2, grouping1)
        proj_3 = partition(student_list, grouping2)

        score = 0
            
        for r in range (num_students):          
            gr1 = np.asarray([item for item in proj_1 if r in item])
            gr2 = np.asarray([item for item in proj_2 if r in item])
            gr3 = np.asarray([item for item in proj_3 if r in item])
            args = [gr1, gr2, gr3]
            groups  = np.concatenate(args, axis=1)
            unique_ids = len(np.unique(groups))
            num_ids = np.shape(groups)[1]
            if num_ids == unique_ids + 2:
                score += 0
            else:
                score += num_ids-unique_ids
        print(score)
        if score <=8:
            found = 1
    return(proj_1, proj_2, proj_3)
            
    
def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

def partition (list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]

proj_1, proj_2, proj_3 = getGroups(student_list, 17, 10, 50)
