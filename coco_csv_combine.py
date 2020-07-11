# 2 simple file merge

import os

base_dir = os.getcwd()
csv_dir = os.path.join(base_dir, 'csv/') # directory for csv files
out_dir = os.path.join(base_dir, 'unity') # directory for output csv file

out_file = open(os.path.join(out_dir, 'merged.csv'), 'w') # file write

files = os.listdir(csv_dir) # list of csv files

for filename in files:
    if ".csv" not in filename:
        continue
    file = open(csv_dir + filename)
    for line in file:
        out_file.write(line)
    out_file.write("\n")
    file.close()
out_file.close()

# endmodule

# use excel for sorting order ^^7
