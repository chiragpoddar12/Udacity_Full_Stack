import os

def rename_files():
    filelist = os.listdir(r"C:\Chirag\Udacity Full Stack Web Development\Project 1\prank")
    print filelist
    savedDir = os.getcwd()
    os.chdir(r"C:\Chirag\Udacity Full Stack Web Development\Project 1\prank")
    for filename in filelist:
       os.rename(filename, filename.translate(None, "0123456789"))
    #os.rename("athens.jpg","austin.jpg")
    os.chdir(savedDir)

rename_files()
