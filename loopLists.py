#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : sunny-io
# Created Date: 2021-09-18
# =============================================================================
"""In case you have a bunch of lists, loop through list of csvs and list of compilation names. Edit lists in this code"""

from Classs_ID3TagAudio import ID3TagAudio
import os
wd = input('Enter the name of the folder for CSV and Audio files:')
os.chdir(wd)
print(os.getcwd())

append_file_extension = '.mp3'
header = 2

lists = ['Abriss']
csvs = ['Abriss.CSV']

for item in csvs:
    name = lists[csvs.index(item)]

    name = ID3TagAudio([header, append_file_extension, name])
    name.set_audio_meta_list(item)
