# Eyed3FromCSV

Set ID 3v2_3 Tags for MP3 files. Configured for tagging Interview MP3 from 4 column ExcelSheet CSV export
No Warrenty. I didn't encouter any problems, but I still keep backup copies of the audio files.

Current configuration:
Configured for tagging Interview-MP3 from 4 column ExcelSheet CSV export

- column[0] - track number
- column[1] - file name
- column[2] - artist
- column[3] - title
- genre set to 101 Speech
- album title, no of header lines, csv file name as input parameter=> input prompt in setMeta.py

## Files:

Classs_ID3TagAudio.py - this does the actual work

setMeta.py - simple text prompt to read one csv and set meta data. Verbose
loopLists - csvs and lists lists provided for looping through several csvs, edit lists in source. Prompt for csv location

# Set up for flexible configuration

- available in v 0.5 (class methods expect params, setMeta.py prompts for those, ):
  - optionally append file extension to file-column on read in
  - set number of header lines
  - album title
  - cvs file name
  - path to csv folder (required to set working directory)
