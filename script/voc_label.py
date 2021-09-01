import copy
import xml.etree.ElementTree as ET
import cv2
import os
from os import listdir, getcwd
from os.path import join


classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42"]

# box?????ROI????????(x,y????????)
# ????ROI???????????????,?ROI?w?h??????????
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.08
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x, y, w, h)
 
 
# ????xml???
def convert_annotation(image_add):
    # image_add????????.jpg
    #image_add = os.path.split(image_add,' ')[1]  # ?????
    image_name = image_add.split()[0]
    print(image_name)
    image_name = image_name.replace('.jpg', '')  # ????,???????
    in_file = open('/home/eza1szh/keras-yolo3-master/VOCdevkit/VOC2007/Annotations/' + image_name + '.xml')  # ?????xml??
    out_file = open('/home/eza1szh/keras-yolo3-master/VOCdevkit/VOC2007/labels/%s.txt' % (image_name)', 'w')
 
    tree = ET.parse(in_file)
    root = tree.getroot()
 
    size = root.find('size')
 
    w = int(size.find('width').text)
    h = int(size.find('height').text)
 
    # ???XML???Object???
    for obj in root.iter('object'):
        # iter()??????????/???????
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # ??????????????????,??difficult = 1,???object
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)#?????,????????,????yolo???cfg??????????
        xmlbox = obj.find('bndbox')
 
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(
            xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
 
 
if not os.path.exists('/home/eza1szh/keras-yolo3-master/VOCdevkit/VOC2007/labels/'):#??????
    os.makedirs('/home/eza1szh/keras-yolo3-master/VOCdevkit/VOC2007/labels/')
 
image_adds = open("/home/eza1szh/keras-yolo3-master/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt")
for image_add in image_adds:
    image_add = image_add.strip()
    convert_annotation(image_add)
 
print("Finished")