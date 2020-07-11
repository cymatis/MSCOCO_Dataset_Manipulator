# 1 extract information from dataset

from pycocotools.coco import COCO # need to be install from external pip
import os
import sys
import pandas as pd

# reset for memory and define directory
cat_of_interest = "bus" # supports only one category.

base_dir = os.getcwd()

# file directory for annotation file
ann_file_dir = os.path.join(base_dir, 'COCOdataset2017/annotations')
ann_file = os.path.join(ann_file_dir, 'instances_val.json')

# output file directory for csv file
out_dir = os.path.join(base_dir, 'cvs')
csv_save_path = os.path.join(out_dir, cat_of_interest + '.csv')

# COCO instance
coco = COCO(ann_file)

# get category id from agument
cat_id  = coco.getCatIds(catNms=[cat_of_interest])

# get annotation ids for current category
ann_ids = coco.getAnnIds(catIds=cat_id, iscrowd=None)
all_ann = coco.loadAnns(ann_ids)

df_rows = []
for i in range(0, len(all_ann)):
    cur_ann    = all_ann[i]
    cbbox      = cur_ann["bbox"]
    cimg_info  = coco.loadImgs(cur_ann["image_id"])

    if(len(cimg_info) > 1):
        print("ERROR: More than one image got loaded")
        sys.exit(1)
        
    filename   = cimg_info[0]["file_name"]
    cur_class  = cat_of_interest
    width    = cimg_info[0]["width"]
    height   = cimg_info[0]["height"]
    xmin     = int(cbbox[0])
    ymin     = int(cbbox[1])
    xmax     = min(int(xmin + cbbox[2]), width-1) # prevent excceeding max width resolution
    ymax     = min(int(ymin + cbbox[3]), height-1) # prevent excceeding max height resolution

    # each rows will be following augments

    df_rows  = df_rows + [[filename, str(width), str(height), cur_class,
                           str(xmin), str(ymin), str(xmax), str(ymax)]]

# giving definition of columns
df=pd.DataFrame(df_rows, columns=["filename", "width", "height", "class",
                           "xmin", "ymin", "xmax", "ymax"])
df.to_csv(csv_save_path)

#endmodule