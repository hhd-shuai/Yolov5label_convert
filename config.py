import os

class_names = ["Regional Defects", "Black Long Warp", "White Weft", "Fuzzy Weft"]
cls_names_map = {"Regional Defects":"区域性缺陷", "Black Long Warp":"黑长经线", "White Weft":"白纬线", "Fuzzy Weft":"模糊纬线"}
expand_pix = 20
random_crop_num = 7

images_path = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/images/train2017"
labels_path = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/labels/train2017"

images_cls_folder = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/images/class_imgs"
save_labels_path = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/labels/cls_labels"
images_binary_cls_folder = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/images/binary_class_imgs"
save_binary_labels_path = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/labels/binary_cls_labels"

val_images_path = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/images/val2017"
val_labels_path = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/labels/val2017"
val_binary_imgs_save_path = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/images/binary_class_imgs_val"
val_binary_labels_save_path = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/labels/binary_cls_val_labels"

original_neg_imgs = "/home/hhd_shuai/data/hengli_fabric/data_恒力/images/train_neg_1"
#/home/hhd_shuai/data/hengli_fabric/data_恒力/images/train2017_neg_images
#/home/hhd_shuai/data/hengli_fabric/data_恒力/images/train_neg_1
neg_imgs_path = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/images/neg_imgs"
neg_labels_path = "/home/hhd_shuai/data/hengli_fabric/yolo_dataset/labels/neg_labels"

est_images_path = "/home/hhd_shuai/PycharmProjects/Yolo2Classifier/data/images"
test_labels_path = "/home/hhd_shuai/PycharmProjects/Yolo2Classifier/data/labels"