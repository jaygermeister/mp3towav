#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jayger
#
# Created:     15/05/2023
# Copyright:   (c) Jayger 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pydub
import tkinter as tk
from tkinter import filedialog
from os import path, mkdir
import numpy as np

def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    sound = pydub.AudioSegment.from_mp3(mp3_file_path)
    sound.export(wav_file_path, format="wav")

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

if file_path.endswith(".mp3"):
    mp3_file_path = file_path
    wav_save_dir = "c:/Wav_save"
    if not path.exists(wav_save_dir):
        mkdir(wav_save_dir)
    wav_file_path = path.join(wav_save_dir, path.basename(mp3_file_path)[:-4] + ".wav")
    convert_mp3_to_wav(mp3_file_path, wav_file_path)
    print(f"Successfully converted {mp3_file_path} to {wav_file_path}")
else:
    print("Please select an MP3 file.")
