import glob
import os

# detect the current working directory and print it
path = os.getcwd()
print("The current working directory is %s" % path)

for file in glob.glob("to_zoia/*.bin"):

    base = os.path.basename(file)
    fileName = os.path.splitext(base)[0]   

    path = f'/patches/{fileName}'.lower()

    print(path)

    # try:
    #     os.mkdir(path)
    # except OSError:
    #     print("Creation of the directory %s failed" % path)
    # else:
    #     print("Successfully created the directory %s " % path)
