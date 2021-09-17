#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : sunny-io
# Created Date: 2021-09-18
# =============================================================================
"""The Module Has Been Build to tag MP3 files from Excel CSV export files.\n
Created for tagging interview-snippet files stored as MP3.\n
Excel provided lists with time/location (mapped to title) and interviewies(mapped to artist).\n
genre set to 101 Speech. 
"""
# =============================================================================
# Imports
#
import eyed3
import os
import csv
import numpy as np

# ==============================================================================


class ID3TagAudio():

    def __init__(self, options=[]):
        # initialise audio group to be processed
        # metafile is the file containing meta data to be set or output target for meta data, must contain a column with file names
        # options: Options list,
        # [0]= number of header lines (not to be processe),
        # [1]= file name extension, if not set in metafile
        # [2]= album title

        self.__columns_fixed = {'genre': '101', 'album': 'Interviews'}

        # column mapping not yet implemented in v0.5
        self.__columns_read = {'file': 1,
                               'track_no': 0, 'title': 3, 'artist': 2}

        if options == []:
            self.__header = 0
            self.__extension = ''

        else:
            self.__header = options[0]  # number of header-lines

            # specifies if '.mp3' has to be appened to fname-column
            self.__extension = options[1]
            self.__columns_fixed['album'] = options[2]

        self.mydata = []  # initialise data list


# read the meta data file

    def get_metafile(self, metafile):
        # method generates list of lists from meta data file
        # metafile must be csv from Excel, delimiter ;

        self.__mycsv = os.path.join(os.getcwd(), metafile)

        self.mydata = []

        # open metadata file
        with open(self.__mycsv, newline='',) as csvfile:

            id3s = csv.reader(csvfile, dialect='excel',
                              delimiter=";", quotechar='|')
            for row in id3s:
                # print (row)
                # append file name extension if set in input params
                row[1] = row[1]+self.__extension

                # append to self.mydata of object instance
                self.mydata.append(row)

        # print (self.mydata, len(self.mydata))

    def get_audio_path(self, fname):
        # generates path from file name
        # careful, path is generated using current working directory, so execute from cwd=location of your audio files

        self.myfile = os.path.join(os.getcwd(), fname)
        # print(self.myfile)
        return self.myfile

# read existing meta data
    def get_audio_meta(self, path):
        # get title, album, artist, genre and track number from audiofile
        output = []

        try:
            audiofile = eyed3.load(path)

            output.append(audiofile.tag.title)
            output.append(audiofile.tag.album)
            output.append(audiofile.tag.artist)
            output.append(audiofile.tag.genre)
            output.append(audiofile.tag.track_num)

        except Exception as e:
            print(type(e), e)

        return output

    # read existing meta data for files in list:

    def get_audio_meta_list(self, filelist):
        # generates list of meta data from list of file names

        output_list = []
        try:
            for i in filelist:  # loop list

                # append what you find
                output_list.append(self.get_audio_meta(i))
        except Exception as e:
            print(type(e), e)

        return output_list


# set audio meta data

    def set_audio_meta(self, file, item):
        # sets audio meta data for one file
        # file is file name/path
        # item is list of values, 0= track no, 1=file name, 2=artist, 3=title
        try:
            audiofile = eyed3.load(file)

            # values fixed for album instance,
            audiofile.tag.album = self.__columns_fixed['album']
            audiofile.tag.genre = self.__columns_fixed['genre']

            # values taken from meta file, position parameters not yet configurable
            audiofile.tag.artist = item[2]
            audiofile.tag.title = item[3]
            audiofile.tag.track_num = int(item[0])

            audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
        except Exception as e:
            print(type(e), e)

    # get list and loop to set meta data
    def set_audio_meta_list(self, metafile):
        # bulk set metadata
        # read file and generate list
        self.get_metafile(metafile)

        # loop through list and set data
        for item in self.mydata[2:-1]:
            # print(item)
            self.set_audio_meta(item[1], item)
