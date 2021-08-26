import os
import sys
import operator
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def get_files_name(f_path):
    files = os.listdir(f_path)
    files_name_list = []
    for file in files:
        if not os.path.isdir(file):
            file_name = file.split('.')[0]
            files_name_list.append(file_name)

    return files_name_list

def txtfile2matrix(filename):
    fr = open(filename)
    number_lines = len(fr.readlines())
    class_label_vector = []
    xywh_matrix = np.zeros((number_lines, 4))
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        list_from_line = line.split(' ')
        class_label_vector.append(int(list_from_line[0]))
        xywh_matrix[index,:] = list_from_line[1:5]
        index += 1
    return class_label_vector, xywh_matrix