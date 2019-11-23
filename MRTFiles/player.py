import os
import sys
import time
import ctypes
import random
import requests
import subprocess
import youtube_dl

ydl_opts = {}
winpy = sys.argv[1]
music = []
played = []

if not os.path.isdir('MRTFIles/Music/'):
    os.mkdir('MRTFIles/Music/')
if os.path.isfile("MRTFIles/YtLinks"):
    with open ("MRTFIles/YtLinks", "r") as handle:
        lines = handle.readlines()
        for line in lines:
            music.append(line.rstrip())
else:
    songs = requests.get('https://pastebin.com/raw/1zwdz16u').text
    lines = songs.split('\n')
    for line in lines:
        music.append(line.rstrip())
while True:
    song = random.choice(music)
    selectedsong = song
    while selectedsong in played:
        song = random.choice(music)
        selectedsong = song
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(selectedsong, download=False)
        video_title = info_dict.get('title', None)
    if os.path.isfile('MRTFIles/Music/{}.wav'.format(video_title)):
        pass
    else:
        ydl_opts = {
            'outtmpl': 'MRTFIles/Music/{}.webm'.format(video_title),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([selectedsong])
    p = subprocess.Popen([winpy,'MRTFIles/play.py','MRTFIles/Music/{}.wav'.format(video_title),str(os.getpid())])
    while p.poll() is None:
        ctypes.windll.kernel32.SetConsoleTitleW("meanwood's raid tool | Playing: {}".format(video_title))
        time.sleep(3)
    played.append(selectedsong)
    if len(played) == len(music):
        break
