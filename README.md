# Lecture-Formatter

SPH E-Learning Services Naming Convention Tool for Formatting File Structure of Lectures
Developed by Xander Elliott

This tool is used to create the file structure needed for lectures pulled from the server.

## An example of this looks as follows:

### ORIGINAL:
```
1234_LectureName:
    -> audio.wav
    -> slides.pptx
    -> script.docx or .txt
```
### FORMATTED:
```
1234_LectureName:
-> Development:
    -> 1234_LectureName_AudioEdit.wav
    -> 1234_LectureName_SlidesEdit.pptx
    -> 1234_LectureName_AudioFinal (folder)

-> Production:

-> Source:
    -> 1234_LectureName_AudioOriginal.wav
    -> 1234_LectureName_SlidesOriginal.wav
    -> 1234_LectureName_ScriptOriginal.docx or .txt

*This tool can be used on multiple lectures at once to save time in renaming files and creating folders.
```

## To use:
```
1. Extract the LectureFormatter.zip file onto your desktop.
2. Drop any lecture folders you want converted into the extracted LectureFormatter folder.
3. Open command prompt and type "cd desktop/LectureFormatter" (or follow the correct navigation path if
   your tool is placed elsewhere) to move into the right directory.
4. Type the command "python LectureFormatter.py" and your folder will now adhere to the correct file structure!

1234_LectureName is included in the tool's folder and can be used as a test for expected output. The file
can safely be deleted if it is not needed.
```

## An example of console output looks like this:
 ```
 ======================================================================
 Formatting 1234_LectureName
 ======================================================================

 Production folder created
 Development folder created
 Source folder created
 ----------------------------------------------------------------------
 Renamed audio.wav to 1234_LectureName_AudioOriginal.wav
 1234_LectureName_AudioEdit.wav created
 Moved 1234_LectureName_AudioOriginal.wav to Source
 Moved 1234_LectureName_AudioEdit.wav to Development
 ----------------------------------------------------------------------
 Renamed script.txt to 1234_LectureName_ScriptOriginal.txt
 Moved 1234_LectureName_ScriptOriginal.txt to Source
 ----------------------------------------------------------------------
 Renamed slides.pptx to 1234_LectureName_SlidesOriginal.pptx
 1234_LectureName_SlidesEdit.pptx created
 Moved 1234_LectureName_SlidesOriginal.pptx to Source
 Moved 1234_LectureName_SlidesEdit.pptx to Development

 ======================================================================
 Lecture Formatting Finished!
 ======================================================================
 ```