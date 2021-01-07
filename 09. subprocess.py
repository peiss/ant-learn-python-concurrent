import subprocess

"""
proc = subprocess.Popen(
    ["start", "./datas/余生一个浪.mp3"],
    shell=True
)

proc.communicate()

"""

proc = subprocess.Popen(
    [r"C:\Program Files\7-Zip\7z.exe",
     "x",
     "./datas/7z_test.7z",
     "-o./datas/extract_7z",
     "-aoa"],
    shell=True
)

proc.communicate()
