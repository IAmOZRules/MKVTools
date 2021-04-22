# MKVTools
Python script to rename episodes, subtitles (from IMDb) and video tags (changed to video file title).

#### Usage
```
usage: python rename.py [-h] -c <code> [options]

optional arguments:
  -h, --help        show this help message and exit
  -c , --code       IMDb CODE for the Series
  -e , --episode    Rename EPISODES of the series in the specified Directory
  -s , --subtitle   Rename SUBTITLES of the Series in the Directory
  -t , --tag        Rename VIDEO TAGS for MKV Videos
```

#### Example
```
python rename.py -c tt000472954 -e "D:\Episode Directory" -s "D:\Subtitle Directory" -t "D:\Episode Directory"
```

### NOTES:
- Make sure that **ALL** episodes/subtitles are available in the one folder, not nested folders!
- Due to certain limitations not yet handled by me, ensure that the **Episodes and Subtitles are in separate folders**!

### TODO:
- [x] Convert separate scripts into a single CLI operation
- [ ] Add custom season/episode range to be renamed
- [ ] Renaming in nested directories
- [ ] Maybe a GUI 🤷‍♂️
