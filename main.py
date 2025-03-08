import os

from resize import resize_image

input_dir = '/mnt/c/Users/bernardo.silva/Pictures/Retratos dos Crachás'
files = os.listdir(input_dir)

output_dir = 'outputs'

for file in files:
    if file.endswith('jpg'):
        resize_image(input_dir + '/' + file, output_dir, (100, 140))
