from pathlib import Path
from os import listdir
from os.path import isfile, join


downloads_path = str(Path.home() / "Downloads")
clean_path = str(Path.home() / "Downloads" / "Clean")

files = [f for f in listdir(downloads_path) if isfile(join(downloads_path, f))]

# create the clean folder if it doesn't exist
Path(clean_path).mkdir(parents=True, exist_ok=True)

pdf_path = str(Path.home() / "Downloads" / "Clean" / "Pdf")
Path(pdf_path).mkdir(parents=True, exist_ok=True)

images_path = str(Path.home() / "Downloads" / "Clean" / "Images")
Path(images_path).mkdir(parents=True, exist_ok=True)

zips_path = str(Path.home() / "Downloads" / "Clean" / "Zips")
Path(zips_path).mkdir(parents=True, exist_ok=True)

doc_path = str(Path.home() / "Downloads" / "Clean" / "Docs")
Path(doc_path).mkdir(parents=True, exist_ok=True)

excel_path = str(Path.home() / "Downloads" / "Clean" / "Excel")
Path(excel_path).mkdir(parents=True, exist_ok=True)

jar_path = str(Path.home() / "Downloads" / "Clean" / "Jars")
Path(jar_path).mkdir(parents=True, exist_ok=True)

exe_path = str(Path.home() / "Downloads" / "Clean" / "Exe")
Path(exe_path).mkdir(parents=True, exist_ok=True)

videos_path = str(Path.home() / "Downloads" / "Clean" / "Videos")
Path(videos_path).mkdir(parents=True, exist_ok=True)

sounds_path = str(Path.home() / "Downloads" / "Clean" / "Sounds")
Path(sounds_path).mkdir(parents=True, exist_ok=True)

for file in files:
    if file.endswith(".pdf"):
        # move the file to the pdf folder
        Path(downloads_path + "/" + file).replace(pdf_path + "/" + file)
        print("Moved " + file + " to " + pdf_path)
    elif file.endswith(".zip") or file.endswith(".7z") or file.endswith(".rar"):
        # move the file to the zips folder
        Path(downloads_path + "/" + file).replace(zips_path + "/" + file)
        print("Moved " + file + " to " + zips_path)
    elif file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".HEIC") or file.endswith(".bmp") or file.endswith(".webp") or file.endswith(".gif") or file.endswith(".jfif"):
        # move the file to the images folder
        Path(downloads_path + "/" + file).replace(images_path + "/" + file)
        print("Moved " + file + " to " + images_path)
    elif file.endswith(".doc") or file.endswith(".docx") or file.endswith(".odt") or file.endswith(".txt") or file.endswith(".rtf"):
        # move the file to the docs folder
        Path(downloads_path + "/" + file).replace(doc_path + "/" + file)
        print("Moved " + file + " to " + doc_path)
    elif file.endswith(".xls") or file.endswith(".xlsx"):
        # move the file to the excel folder
        Path(downloads_path + "/" + file).replace(excel_path + "/" + file)
        print("Moved " + file + " to " + excel_path)
    elif file.endswith(".jar"):
        # move the file to the jars folder
        Path(downloads_path + "/" + file).replace(jar_path + "/" + file)
        print("Moved " + file + " to " + jar_path)
    elif file.endswith(".exe"):
        # move the file to the exe folder
        Path(downloads_path + "/" + file).replace(exe_path + "/" + file)
        print("Moved " + file + " to " + exe_path)
    elif file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".avi") or file.endswith(".webm") or file.endswith(".flv") or file.endswith(".mov"):
        # move the file to the videos folder
        Path(downloads_path + "/" + file).replace(videos_path + "/" + file)
        print("Moved " + file + " to " + videos_path)
    elif file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".flac") or file.endswith(".ogg") or file.endswith(".m4a"):
        # move the file to the sounds folder
        Path(downloads_path + "/" + file).replace(sounds_path + "/" + file)
        print("Moved " + file + " to " + sounds_path)