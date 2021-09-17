#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : sunny-io
# Created Date: 2021-09-18
# =============================================================================
"""This script prompts for required data and executes the bulk set of the metadata.\n
    Promps for:
    - album name to be set with this import
    - name of the CSV file to be used
    - number of header lines
    - does your meta data file come with complete audio file names (Y) or do we need to add '.mp3' while processing (N)
"""

from Classs_ID3TagAudio import ID3TagAudio
import numpy as np

print(f"This script reads a 4-column Excel CSV export file and bulk sets the following ID3v2 tags:\n    - artist, title and track from the file, \n- album title from prompt.\nPromps for:\n- album name to be set with this import\n- name of the CSV file to be used\n- number of header lines\n- does your meta data file come with complete audio file names(Y) or do we need to add '.mp3' while processing(N)\nMAKE SURE CSV and Audiofiles both reside in cwd!")


# query album name, csv file name, and number of header lines

list_name = input('Enter the name of the compilation/album:')

csv_name = input(
    'Enter the CSV file name, e.g. user-interviews-project001.csv: ')

header = input('Enter the number of header lines in CSV: ')

qfne = input('Does your CSV hold complete audio file names(Y/N), e.g. 001004.mp3 (Y) or just the base name without extension, e.g. 001004 and we need to append the extension on the fly (N) ?')

# fixed file name extension
if qfne == "N":
    append_file_extension = '.mp3'
else:
    append_file_extension = ''

# create instance, generate meta
album1 = ID3TagAudio([header, append_file_extension, list_name])
album1.get_metafile(csv_name)

# generate list for checking changed data
file_list = np.array(album1.mydata)[:, 1]

print(f"Aktuelle Metadaten: {album1.get_audio_meta_list(file_list)}")

# set meta data
album1.set_audio_meta_list(csv_name)


print(f"Geänderte Metadaten: {album1.get_audio_meta_list(file_list)}")
