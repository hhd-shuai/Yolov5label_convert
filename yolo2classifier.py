import os

from config import *
from utils import file_util
from utils import img_operate_util

def generate_cls_folder(folder_path, class_names):
    for clsname in class_names:
        if not os.path.exists(os.path.join(folder_path, clsname)):
            os.makedirs(os.path.join(folder_path, clsname))

def crop_imgs(f_path, lab_path, cropped_img_save_path, lab_save_path, expand_p):
    files = os.listdir(f_path)
    files_name_list = []

    for file in files:
        if not os.path.isdir(file):
            cropped_save_path = []
            file_name = file.split('.')[0]
            print("Cropping " + file_name)
            files_name_list.append(file_name)
            lab_file_name = file_name + '.txt'
            cls_label_vec, xywh_matrix = file_util.txtfile2matrix(os.path.join(lab_path, lab_file_name))
            cls_names = [class_names[cls] for cls in cls_label_vec]
            img_file = os.path.join(f_path, file)
            img_operate_util.crop_img_and_write(img_file, cls_names, xywh_matrix, file_name,
                                                cropped_img_save_path, lab_save_path, expand_p)

    print("Complete.")

def crop_neg_imgs(f_path, neg_img_path, neg_lab_path, crop_num):
    files = os.listdir(f_path)
    files_name_list = []

    for file in files:
        if not os.path.isdir(file):
            cropped_save_path = []
            file_name = file.split('.')[0]
            print("Cropping " + file_name)
            files_name_list.append(file_name)
            img_file = os.path.join(f_path, file)
            img_operate_util.random_crop_img_and_write(img_file, file_name, neg_img_path,
                                                       neg_lab_path, crop_num)

    print("Complete.")



if __name__ == "__main__":
    print('..')
    generate_cls_folder(images_cls_folder, class_names)
    if not os.path.exists(val_binary_imgs_save_path):
        os.makedirs(val_binary_imgs_save_path)
    if not os.path.exists(val_binary_labels_save_path):
        os.makedirs(val_binary_labels_save_path)

    crop_imgs(val_images_path, val_labels_path, val_binary_imgs_save_path,
              val_binary_labels_save_path, expand_pix)

    # crop_neg_imgs(original_neg_imgs, neg_imgs_path, neg_labels_path, random_crop_num)