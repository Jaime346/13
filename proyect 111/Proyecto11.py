import os
import shutil
from_dir="/Users/jaimerosas/Downloads"
to_dir="/Users/jaimerosas/Downloads/Documentos_archivos"
list_of_files= os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extensions=os.path.splitext(file_name)

if extensions == "":
  continue
if extensions in [".txt",".doc",".docx",".pdf"]:

  path1=from_dir+"/"+file_name
  path2=to_dir+"/"+"Images_files"
  path3=to_dir+"/"+"Images_files"+"/"+file_name
  print("path1",path1)
  print("path3",path3)

  if os.path.exists(path2):
     print("Moving"+file_name+".....")

     shutil.move(path1,path3)

  else:
     os.makedirs(path2)
     print("Moving"+file_name+".....")
     shutil.move(path1,path3)