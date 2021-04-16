import csv
import glob
import os
import re
from shutil import copyfile
import os.path
from mdutils.mdutils import MdUtils

path = os.getcwd()
print("The current working directory is %s" % path)

default = {}

for i in range(0, 64):
    default[i] = [
        f'./patches/blank/_zoia.bin',
        f'./to_zoia/{i:03d}_zoia_blank.bin'
    ]

for file in glob.glob("./to_zoia/**/*.bin"):
    os.remove(file)

with open('./to_zoia_patches.csv', newline='') as csvfile:
    patches = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in patches:
        patchNumber = int(row["patchNumber"])
        patchName = row["patchName"]
        source = f'./patches/{patchName}/_zoia.bin'
        default[patchNumber] = [
            source,
            f'./to_zoia/{patchNumber:03d}_zoia_{patchName}.bin'
        ]

for key, value in default.items():
    print(key, '->', value[0], value[1])
    if(os.path.isfile(value[0])):
        copyfile(value[0], value[1])
