# .csv-->.xml
# ! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image
import csv
import os
import numpy as np
import random
import requests

source_path = './label_new/'
CsvFile = os.listdir(source_path)
for i in range(len(CsvFile)):
# read csv 1 without width and height

    file_path =str('./label_new/' + CsvFile[i])
    with open(file_path) as csvfile:
        csv_reader = csv.reader(csvfile)  # ??csv.reader??csvfile????
        birth_header = next(csv_reader)  # ???????????
        count = 0
        img_pre = ''
        flag = 0
        for row in csv_reader:  # ?csv ?????????birth_data?
            #print(row)
            #first
            if flag == 0:
                img_pre = row[0].split(';')[0]
                flag = 1
                xml_file = open(('./VOCdevkit/VOC2007/Annotations/' + img_pre + '.xml'), 'w')
                xml_file.write('<annotation>\n')
                xml_file.write('    <folder>VOC2007</folder>\n')
                xml_file.write('    <filename>' + str(img_pre) +'.jpg' +  '</filename>\n')
            img = row[0].split(';')[0]
            # new file
            if img != img_pre:
                # close file
                xml_file.write('</annotation>')
                xml_file.close()
                # new file
                xml_file = open(('./VOCdevkit/VOC2007/Annotations/' + img + '.xml'), 'w')
                xml_file.write('<annotation>\n')
                xml_file.write('    <folder>VOC2007</folder>\n')
                xml_file.write('    <filename>' + str(img)  +'.jpg' +  '</filename>\n')
            #print(img)


            xml_file.write('    <size>\n')
            xml_file.write('        <width>' + str(row[0].split(';')[1]) + '</width>\n')
            xml_file.write('        <height>' + str(row[0].split(';')[2]) + '</height>\n')
            xml_file.write('        <depth>3</depth>\n')
            xml_file.write('    </size>\n')



            xml_file.write('    <object>\n')
            xml_file.write('        <name>' + str(row[0].split(';')[7]) + '</name>\n')
            xml_file.write('        <pose>Unspecified</pose>\n')
            xml_file.write('        <truncated>0</truncated>\n')
            xml_file.write('        <difficult>0</difficult>\n')
            xml_file.write('        <bndbox>\n')
            xml_file.write('            <xmin>' + str(row[0].split(';')[3]) + '</xmin>\n')
            xml_file.write('            <ymin>' + str(row[0].split(';')[4]) + '</ymin>\n')
            xml_file.write('            <xmax>' + str(row[0].split(';')[5]) + '</xmax>\n')
            xml_file.write('            <ymax>' + str(row[0].split(';')[6]) + '</ymax>\n')
            xml_file.write('        </bndbox>\n')
            xml_file.write('    </object>\n')
            print(str(row[0].split(';')[0])+': Finished')

