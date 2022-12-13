from PIL import Image
import os
import shutil

folderToClean = input("What folder you want to sort? (Copy the directory from your explorer): ")
fileType = input("What type of files you want to move? (Documents, Images, Videos or Audios): ")
newDirectory = input(
    "Where do you want to move the files? (Copy the directory from your explorer ")

imagesExt = ['.png', '.apng', '.jpg', '.jpeg', '.avif', '.gif', '.svg', '.webp']
vidExt = ['.mp4', '.mov', '.wnv', '.avi', '.avchd', '.flv', '.mkv', '.webm', '.mpg']
audExt = ['.mp3', 'mpeg-1', '.aac', '.wav']
docsExt = ['.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.zip', '.rar', '.torrent']


def cleanFolders(folder, newFolder, ft):
    try:
        os.listdir(newFolder)
        for filename in os.listdir(folder):
            name, extensions = os.path.splitext(folder + filename)
            if(ft == "Images" or ft == "images" and extensions in imagesExt):
                oldPath = folder + "/" + filename
                newPath = newFolder + "/" + filename
                shutil.move(oldPath, newPath)
            if (ft == "Documents" or ft == "documents" and extensions in docsExt):
                oldPath = folder + "/" + filename
                newPath = newFolder + "/" + filename
                shutil.move(oldPath, newPath)
            if (ft == "Audios" or ft == "audios" and extensions in audExt):
                oldPath = folder + "/" + filename
                newPath = newFolder + "/" + filename
                shutil.move(oldPath, newPath)
            if (ft == "Videos" or ft == "videos" and extensions in vidExt):
                oldPath = folder + "/" + filename
                newPath = newFolder + "/" + filename
                shutil.move(oldPath, newPath)
            else:
                print("Couldn't find {} on this directory".format(ft))
    except:
        print("Couldn't find the {} directory. Check if it exist or create one ✌️".format(newFolder))


cleanFolders(folderToClean, newDirectory, fileType)
