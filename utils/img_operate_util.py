import os.path

import cv2
import torch
import numpy as np
import json

def xywh2xyxy(x):
    # Convert nx4 boxes from [x, y, w, h] to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
    y = torch.zeros_like(x) if isinstance(x, torch.Tensor) else np.zeros_like(x)
    y[:, 0] = x[:, 0] - x[:, 2] / 2  # top left x
    y[:, 1] = x[:, 1] - x[:, 3] / 2  # top left y
    y[:, 2] = x[:, 0] + x[:, 2] / 2  # bottom right x
    y[:, 3] = x[:, 1] + x[:, 3] / 2  # bottom right y
    return y

def cls_anno_json(cls):
    gt_json = [{"name": "是否有缺陷",
        "tagID": "1430717766209667072",
        "value": "是"}]
    return gt_json

def neg_anno_json():
    gt_json = [{"name": "是否有缺陷",
        "tagID": "1430717766209667072",
        "value": "否"}]
    return gt_json

def crop_img_and_write(im_file, cls_names, xywh_metrix, f_name, img_save_path, lab_save_path, expand_p):
    img = cv2.imread(im_file)
    h, w, c = img.shape
    positions = xywh2xyxy(xywh_metrix)
    rows, cols = positions.shape
    assert rows == len(cls_names)
    for row in range(rows):
        x0, y0, x1, y1 = positions[row, :]
        half_expand_p = expand_p / 2
        x0 = int((x0 - half_expand_p if x0 - half_expand_p > 0 else x0) * w)
        y0 = int((y0 - half_expand_p if y0 - half_expand_p > 0 else y0) * h)
        x1 = int((x1 + half_expand_p if x1 + half_expand_p < w else x1) * w)
        y1 = int((y1 + half_expand_p if y1 + half_expand_p < h else y1) * h)
        cropped = img[y0:y1, x0:x1] #[y0,y1  x0,x1]
        cls_name = cls_names[row]
        lab_json = cls_anno_json(cls_name)
        im_f_name = f_name + "v_" + str(row) + ".jpg"
        lab_f_name = f_name + "v_" + str(row) + ".json"
        # s_img_path = os.path.join(img_save_path, cls_name, im_f_name)
        s_img_path = os.path.join(img_save_path, im_f_name)
        s_lab_path = os.path.join(lab_save_path, lab_f_name)
        cv2.imwrite(s_img_path, cropped)
        print("Cropped img " + im_f_name + " is saved.")
        with open(s_lab_path,'w') as file_obj:
            json.dump(lab_json, file_obj)
        print("Label " + lab_f_name + " is saved.")

def random_crop_img_and_write(im_file, f_name, neg_img_path, neg_lab_path, crop_num):
    img = cv2.imread(im_file)
    h, w, c = img.shape
    for i in range(crop_num):
        x = np.random.randint(0, w - 50)
        y = np.random.randint(0, h - 50)
        crop_w = np.random.randint(50, w - x)
        crop_h = np.random.randint(50, h - y)
        cropped = img[y:y + crop_h, x:x + crop_w]
        neg_annos_json = neg_anno_json()
        im_f_name = f_name + "n2_" + str(i) + ".jpg"
        lab_f_name = f_name + "n2_" + str(i) + ".json"
        s_img_path = os.path.join(neg_img_path, im_f_name)
        s_lab_path = os.path.join(neg_lab_path, lab_f_name)
        cv2.imwrite(s_img_path, cropped)
        print("Neg img " + im_f_name + " is saved.")
        with open(s_lab_path,'w') as file_obj:
            json.dump(neg_annos_json, file_obj)
        print("Neg label " + lab_f_name + " is saved.")
