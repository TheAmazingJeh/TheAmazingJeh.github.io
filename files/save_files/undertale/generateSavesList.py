import os, json

# get all the save files in the directory
def get_save_files(path):
    filesNew = []
    files = os.listdir(path)
    for file in files:
        if file.endswith(".zip"):
            filesNew.append(file)
    print(json.dumps(filesNew, indent=4))