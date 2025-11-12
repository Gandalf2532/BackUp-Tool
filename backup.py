import os
import zipfile

def backupfolder_and_zip(source, target, zipname):
    files_in_dir = []
    for r, d, f in os.walk(source):
       for item in f:
          files_in_dir.append(os.path.join(r,item))

    os.makedirs(target, exist_ok=True)

    zip_path = os.path.join(target, zipname)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files_in_dir:
            rel_path = os.path.relpath(file, source)
            zipf.write(file, rel_path)