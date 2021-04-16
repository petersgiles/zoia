import glob
import os
import re
from shutil import copyfile
import os.path

# detect the current working directory and print it
path = os.getcwd()
print("The current working directory is %s" % path)

for file in glob.glob("downloads/*.bin"):

    base = os.path.basename(file)
    fileName = os.path.splitext(base)[0].lower()

    fileName = re.sub(r'\s+', '_', fileName)
    fileName = re.sub(r'^[0-9]+_zoia_', '', fileName)
    fileName = fileName.strip()

    directory = f'./patches/{fileName}'

    if(fileName):
        try:
            if(not os.path.exists(directory)):
                os.mkdir(directory)

            readme_path = f'{directory}/README.MD'
            if(os.path.isfile(readme_path)):
                readme = open(readme_path, "w")
                pageTitle = fileName.replace("_", " ").capitalize()
                readme.write(f'# {pageTitle}')

            patch_path = f'{directory}/_zoia.bin'
            if(not os.path.isfile(patch_path)):
                copyfile(file, patch_path)

        except OSError as error:
            print(error)
            print("Creation of the directory %s failed" % path)
