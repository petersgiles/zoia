import csv
import glob
import os
import re
from shutil import copyfile
import os.path
from mdutils.mdutils import MdUtils

path = os.getcwd()
print("The current working directory is %s" % path)
for file in glob.glob("patches/**/*.md"):
    os.remove(file)
    

with open('patches/zoia_patches.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:

        patchNumber = row["Factory Patch"]
        patchName = row["Patch Name"]
        description = row["Description"]
        author = row["Author"]
        pedal = row["Expression Pedal/External Switch Functionality"]
        stomp = row["Left Stompswitch Functionality"]

        folderName = re.sub(r'\s+', '_', patchName).lower()
        folderName = folderName.strip()
        directory = f'./patches/{folderName}'

        readme_path = f'{directory}/README'
        pageTitle = patchName.capitalize()
        mdFile = MdUtils(file_name=readme_path)
        mdFile.new_header(level=1, title=pageTitle)
        mdFile.new_header(level=2, title="Factory Patch")
        mdFile.new_paragraph(patchNumber)
        mdFile.new_header(level=2, title="Author")
        mdFile.new_paragraph(author)
        mdFile.new_header(
            level=2, title="Expression Pedal/External Switch Functionality")
        mdFile.new_paragraph(pedal)
        mdFile.new_header(level=2, title="Left Stompswitch Functionality")
        mdFile.new_paragraph(stomp)
        mdFile.create_md_file()
