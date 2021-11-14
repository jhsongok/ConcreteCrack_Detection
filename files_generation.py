import os

current_path = os.path.abspath(os.curdir)

COLAB_ACCESS_PATH = '/content/gdrive/MyDrive/ConcreteCrack_Detection'

YOLO_FORMAT_PATH = current_path + '/custom'
TRAIN_IMAGE_PATH = current_path + '/dataset/train'
TEST_IMAGE_PATH = current_path + '/dataset/valid'

class_count = 0
train_paths = []
test_paths = []

if not os.path.exists('/content/custom'):
  os.makedirs('/content/custom')

# classes. names 파일 생성
with open(YOLO_FORMAT_PATH + '/' + 'classes.names', 'w') as names, \
     open(current_path + '/dataset/train/' + '_darknet.labels', 'r') as txt:
    for line in txt:
        names.write(line)  
        class_count += 1
    print ("[classes.names] is created")

# custom_data.data 파일 생성
with open(YOLO_FORMAT_PATH + '/' + 'custom_data.data', 'w') as data:
    data.write('classes = ' + str(class_count) + '\n')
    data.write('train = ' + COLAB_ACCESS_PATH + '/custom/' + 'train.txt' + '\n')
    data.write('valid = ' + COLAB_ACCESS_PATH + '/custom/' + 'test.txt' + '\n')
    data.write('names = ' + COLAB_ACCESS_PATH + '/custom/' + 'classes.names' + '\n')
    data.write('backup = backup')
    print ("[custom_data.data] is created")

os.chdir(TRAIN_IMAGE_PATH)
for current_dir, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.jpg'):
            image_path = COLAB_ACCESS_PATH + '/dataset/train/' + f
            train_paths.append(image_path + '\n')


os.chdir(TEST_IMAGE_PATH)
for current_dir, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.jpg'):
            image_path = COLAB_ACCESS_PATH + '/dataset/test/' + f
            test_paths.append(image_path + '\n')


# train.txt 파일 생성
with open(YOLO_FORMAT_PATH + '/' + 'train.txt', 'w') as train_txt:
    for path in train_paths:
        train_txt.write(path)
    print ("[train.txt] is created")

# test.txt 파일 생성
with open(YOLO_FORMAT_PATH + '/' + 'test.txt', 'w') as test_txt:
    for path in test_paths:
        test_txt.write(path)
    print ("[test.txt] is created")

