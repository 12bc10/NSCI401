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
student_list = np.append(student_list,100)
combinations_object = itertools.combinations(a_list, 3)
combinations_list = list(combinations_object)

print("there are {} combinations".format(len(combinations_list)))



def getGroups(student_list, number_groups, number_students):
    proj_1 = list(grouper(3, range(num_students)))
    proj_1[-1] = [proj_1[-1][0], proj_1[-1][1], 100]
    found = 0
    
    while found == 0:
        proj_2 = partition(student_list, number_groups)
        score = 0
            
        for r in range (num_students):          
            groups  = np.array([np.asarray([item for item in proj_1 if r in item]), np.asarray([item for item in proj_2 if r in item])])
            unique_ids = len(np.unique(np.ndarray.flatten(groups)))
            num_ids = np.shape(groups[0])[1] + np.shape(groups[1])[1]
            if num_ids == unique_ids + 1:
                score += 0
            else:
                score += 1
        print(score)
        if score == 0:
            found = 1
    return(proj_1, proj_2)
            
    
def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

def partition (list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]

proj_1, proj_2 = getGroups(student_list, 17, 50)
