import os
import shutil


def createIfNotExists(folder): 
    if not os.path.exists(folder): # checks if the same name folder exists in current directory 
        os.makedirs(folder) # making a folder named in the current directory.
        print(f"{folder} folder created")
    else:
        print(f"{folder} folder Exists")

# Moving files according to their extension
def move(folderName,files):
    count = 0    
    for file in files:
        os.replace(file,f"{folderName}/{file}")
        count = count + 1
    print(f"{count} files moved in {folderName}")    


if __name__ == "__main__":
        files = os.listdir() # listing all the files/documents whatever available in the current  directory
        files.remove("main.py") # removing "main.py" from the files

        # making folders
        createIfNotExists("Images") 
        createIfNotExists("Docs")
        createIfNotExists("Media")
        createIfNotExists("Others")

        imgExts = ['.png','.jpg','.jpeg','.tif'] # possible extension of image type

        # making list comprehension
        # segragating extension from files
        # converting extension to lower case
        # segregating files as per their extension
        images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]


        docExts = ['.txt','.pdf','.xlsx','.docs']
        docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


        mediaExts = ['.mp4','.mp3','.flv']
        medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]


        others = []
        # checking if none of the type of file is available then it moves to others
        for file in files:
            ext = os.path.splitext(file)[1].lower() 
            if (ext not in imgExts) and (ext not in mediaExts) and (ext not in docExts) and os.path.isfile(file):
                others.append(file)

        move("Images", images)
        move("Docs", docs)
        move("Media",medias)
        move("Others", others)

