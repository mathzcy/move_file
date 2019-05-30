import os
import shutil
if __name__ =="__main__":
    rootname = "C:\\Users\\18069\\Desktop\\a\\"
    if os.path.exists(rootname) is True:
        names = os.listdir(rootname)
        for i in names:
            folder_name = os.path.join(rootname,i)
            if os.path.isdir(folder_name) is True:
                filename_list = os.listdir(folder_name)
                for filename in filename_list:
                    file = os.path.join(folder_name,filename);
                    print(file)
                    shutil.copy(file,rootname)
