# 3 transform to YOLO format
import os

base_dir = os.getcwd()
csv_dir = os.path.join(base_dir, 'unity/merged.csv') # directory for csv files
out_dir = os.path.join(base_dir, 'final/val/') # train or val

read_file = open(csv_dir, mode='rt') # read-only

line = read_file.readline() # initial line read
previous_name = 'NULL'
cnt = 0

while line:
    
    image_name_raw, img_width, img_height, class_name, xmin, ymin, xmax, ymax = line.split(',')
    
    print(line.split(','))

    image_name, ext = image_name_raw.split('.')
    ymin = ymin.replace('\n','')

    print(previous_name)
    print(image_name)

    if image_name == previous_name:
        pass
    else:
        try:
            write_file.close()
        except:
            pass
        
        write_file = open(os.path.join(out_dir, image_name + '.txt'), mode='wt')
        print("make new!")
        previous_name = image_name   

    img_width = int(img_width)
    img_height = int(img_height)

    xmin = int(xmin)
    ymin = int(ymin)
    xmax = int(xmax)
    ymax = int(ymax)

    pct_xmin = round(float(xmin / img_width), 6)
    pct_ymin = round(float(ymin / img_height), 6)
    pct_xman = round(float(xmax / img_width), 6)
    pct_yman = round(float(ymax / img_height), 6)

    width = round(float((xmax-xmin)), 6)
    height = round(float((ymax-ymin)), 6)
    x_center = round(float((xmin) + (width)), 6)
    y_center = round(float((ymin) + (height)), 6)

    pct_x_center = round(float(x_center / img_width), 6)
    pct_y_center = round(float(y_center / img_height), 6)
    pct_width = round(float(width / img_width), 6)
    pct_height = round(float(height / img_height), 6)

    if pct_x_center > 1:
        print("percentage center_X value is bigger than 1.0")
    elif pct_y_center > 1:
        print("percentage center_Y value is bigger than 1.0")

    xmin = str(xmin)
    ymin = str(ymin)
    xmax = str(xmax)
    ymax = str(ymax)
    x_center = str(x_center)
    y_center = str(y_center)
    width = str(width)
    height = str(height)
    pct_x_center = str(pct_x_center)
    pct_y_center = str(pct_y_center)
    pct_width = str(pct_width)
    pct_height = str(pct_height)

    #final = class_name + ',' + xmin + ',' + ymin + ',' + xmax + ',' + ymax + '\n'
    #final = class_name + ',' + x_center + ',' + y_center + ',' + width + ',' + height + '\n'
    #final = class_name + ',' + pct_xmin + ',' + pct_ymin + ',' + pct_xmax + ',' + pct_ymax + '\n'
    final = class_name + ',' + pct_x_center + ',' + pct_y_center + ',' + pct_width + ',' + pct_height + '\n'
    print(final)
    write_file.write(final)

    del line # 버퍼 지우기

    line = read_file.readline()


