import os, shutil

print (os.getcwd())

os.chdir("D:\web_scrapper")

print (os.getcwd())


img_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.jpg')]
print (img_files)
folderName = []
for f in img_files:
    folderName = f[:f.index(" Tires")]
    folderName.replace(" ", "")
    print (folderName)
    print (os.path.exists(folderName))
    if not os.path.exists(folderName):
        os.mkdir(folderName,0o777)
        shutil.copy2(os.path.join(os.getcwd(), f),folderName)
    else:
        shutil.copy2(os.path.join(os.getcwd(), f), folderName)