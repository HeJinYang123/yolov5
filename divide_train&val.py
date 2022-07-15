import os

root = '/home/radar/Documents/hjy/dataset/'
train_path = '/home/radar/Documents/hjy/dataset/train_image/'
val_path = '/home/radar/Documents/hjy/dataset/val_image/'
if __name__ == '__main__':
    image_path = root +'images'
    label_path = root +'labels'
    imagelist = os.listdir(image_path)
    labellist = os.listdir(label_path)

    if not os.path.exists(train_path):
        os.makedirs(train_path)
    if not os.path.exists(val_path):
        os.makedirs(val_path)




