# implementation: /home/jqy/data/FullIJCNN2013/all/*.ppm  ->  /home/jqy/data/gtsdb_voc/all/*.jpg
# /home/jqy/data/FullIJCNN2013/00/*.ppm  ->  /home/jqy/data/gtsdb_voc/00/*.jpg
# and el.

from PIL import Image
import os

input_train_path="/fs/scratch/XCSERVER_AI-Initiative/traffic-sign-classification/train_images"
output_train_path = "/home/eza1szh/keras-yolo3-master/train_images"
#input_test_path= "/fs/scratch/XCSERVER_AI-Initiative/traffic-sign-classification/test_images"
voutput_test_path = "/home/eza1szh/keras-yolo3-master/aaa"
 
def batch_image(in_dir, out_dir):
    if not os.path.exists(out_dir):
        print(out_dir, 'is not existed.')
        os.mkdir(out_dir)
 
    if not os.path.exists(in_dir):
        print(in_dir, 'is not existed.')
        return -1
    
    directories = [d for d in os.listdir(in_dir) if os.path.isdir(os.path.join(in_dir, d))]
    for d in directories:
        label_directory = os.path.join(in_dir, d)
        new_directory = os.path.join(out_dir, d)
        out_folder = os.path.exists(out_dir+d)
        if not out_folder:
            os.mkdir(new_directory)
        file_names = [os.path.join(label_directory, f) for f in os.listdir(label_directory) if f.endswith(".ppm")]
        # file_names is every photo which is end with ".ppm"
 
        count = 0
        for files in file_names:
            file_path, extfilename = os.path.split(files)
            filename, extname = os.path.splitext(extfilename)
            out_file = filename + '.jpg'
            # print(filepath,',',filename, ',', out_file)
            im = Image.open(files)
            new_path = os.path.join(new_directory, out_file)
            print(count, ',', new_path)
            count = count + 1
            im.save(new_path)
 
 
 
if __name__ == '__main__':
    #batch_image(input_test_path, output_test_path)
    batch_image(input_train_path, output_train_path)
