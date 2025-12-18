import os
folder_path = "files"
files = os.listdir(folder_path)
for index, filename in enumerate(files):
  old_path = os.path.join(folder_path, filename)
  new_path = os.path.join(folder_path,f"file_{index+1}.txt")
  os.rename(old_path, new_path)

print("Files renamed successfully")
