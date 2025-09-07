#SPH E-Learning Services Naming Convention Tool for Formatting File Structure of Lectures
#Developed by Xander Elliott

import os
import shutil

global_lineLength = len(os.getcwd()) + 22

def formatter(lectureName, dirList, currDir):
    dirList = os.listdir(currDir)

    #Attempting to make the four necessary lecture folders
    try:
        os.mkdir("Production")
        print("Production folder created")
        
    except FileExistsError:
        print("Production folder already exists")

    try:
        os.mkdir("Development")
        print("Development folder created")

        os.chdir(currDir + "Development")
        os.mkdir(lectureName + "_AudioFinal")
        os.chdir(currDir)
        
    except FileExistsError:
        print("Development folder already exists")

    try:
        os.mkdir("Source")
        print("Source folder created")
        
    except FileExistsError:
        print("Source folder already exists")

    print("\n")

    #Structuring loop goes through each file and copies/moves accordingly
    for file in dirList:
        filename, extension = os.path.splitext(file)
        match(extension):
            case (".txt"):
                filename = lectureName + "_ScriptOriginal.txt"
                if (file != filename):
                    os.rename(file, filename)
                    print("Renamed " + file + " to " + filename)
                else:
                    print(".txt file name already matches")

                shutil.move((currDir + filename), (currDir + "Source"))
                print("Moved " + filename + " to Source")
                
            case (".docx"):
                filename = lectureName + "_ScriptOriginal.docx"
                if (file != filename):
                    os.rename(file, filename)
                    print("Renamed " + file + " to " + filename)
                else:
                    print(".docx file name already matches")
                    
                shutil.move((currDir + filename), (currDir + "Source"))
                print("Moved " + filename + " to Source")
                
            case (".pptx"):
                filename = lectureName + "_SlidesOriginal.pptx"
                if (file != filename):
                    os.rename(file, filename)
                    print("Renamed " + file + " to " + filename)
                else:
                    print(".pptx file name already matches")
                
                newSlidesName = lectureName + "_SlidesEdit.pptx"
                with open(newSlidesName, "w") as newSlides:
                    print(newSlidesName + " created")
                    shutil.copy2((currDir + filename), (currDir + newSlidesName))

                newSlides.close()
                shutil.move((currDir + filename), (currDir + "Source"))
                print("Moved " + filename + " to Source")
                shutil.move((currDir + newSlidesName),(currDir + "Development"))
                print("Moved " + newSlidesName + " to Development")
                    
            case (".wav"):
                filename = lectureName + "_AudioOriginal.wav"
                if (file != filename):
                    os.rename(file, filename)
                    print("Renamed " + file + " to " + filename)
                else:
                    print(".wav file name already matches")
              
                newAudioName = lectureName + "_AudioEdit.wav"
                with open(newAudioName, "w") as newAudio:
                    print(newAudioName + " created")
                    shutil.copy2((currDir + filename), (currDir + newAudioName))

                newAudio.close()
                shutil.move((currDir + filename), (currDir + "Source"))
                print("Moved " + filename + " to Source")
                shutil.move((currDir + newAudioName), (currDir + "Development"))
                print("Moved " + newAudioName + " to Development")

        #Don't want any extra lines printed for any missing files     
        if (extension != ""):
            print("\n")
        
def main():
    currDir = os.getcwd()
    dirList = os.listdir(currDir)

    #Beginning of searching the directory and sending folders to formatter function
    for folder in dirList:
        filename, extension = os.path.splitext(folder)
        if (extension != ".py" and extension != ".txt"):
            print("=" * global_lineLength)
            print("Formatting " + folder)
            print(("=" * global_lineLength) + "\n")
            addFolder = ("\\" + folder + "\\")
            os.chdir(currDir + addFolder)
            formatter(folder, dirList, (currDir + addFolder))
    
    print("=" * global_lineLength)
    print("Lecture Formatting Finished!")
    print("=" * global_lineLength)
    
if __name__ == "__main__":
    main()
