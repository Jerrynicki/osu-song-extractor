import os
import datetime
import shutil
import sys

cwd = os.getcwd()
osu_dir = ""

if cwd.replace("\\", "/").split("/")[1] == "Users":
    if os.path.exists("C:/Users/"+cwd.replace("\\", "/").split("/")[2]+"/AppData/Local/osu!"):
        osu_dir = "C:/Users/"+cwd.replace("\\", "/").split("/")[2]+"/AppData/Local/osu!"

if osu_dir == "":
    print("osu! directory not found. Please input it manually.")
    osu_dir = input(":").replace("\\", "/").rstrip("/")

if not os.path.isdir("export"):
    os.mkdir("export")

export_name = "export/"+datetime.datetime.now().isoformat().replace("T", " ").replace(":", "-")
os.mkdir(export_name)

amt = len(os.listdir(osu_dir+"/Songs"))

sys.stdout.write("["+" "*amt+"]")
sys.stdout.flush()
sys.stdout.write("\b"*(amt+1))

for song_dir in os.listdir(osu_dir+"/Songs"):
    try:
        int(song_dir.split(" ")[0])
        name = " ".join(song_dir.split(" ")[1:])
    except ValueError:
        name = song_dir

    for file in os.listdir(osu_dir+"/Songs/"+song_dir):
        if file.endswith(".mp3"):
            shutil.copy(osu_dir+"/Songs/"+song_dir+"/"+file, export_name+"/"+name+".mp3")
            sys.stdout.write("-")
            sys.stdout.flush()

print("\n"+str(len(os.listdir(export_name)))+" files saved to "+export_name)
