# MKVTools

Python script to rename episodes and subtitles (names taken from from IMDb) and video tags (changed to video file title for matroska files).

## Usage:

Make sure you have all the requirements installed!

If you dont, simply run `pip install -r requirements.txt` in any terminal, and you are good to go!

To use the tags renaming function, you need to have `mkvpropedit` from [MKVToolNix](https://mkvtoolnix.download/) added to your System PATH.

```
usage: python rename.py [-h] [options]

optional arguments:
  -h, --help            show this help message and exit
  -c , --code           IMDb CODE for the Series
  -r  [ ...], --range  [ ...]
                        Season range for rename
  -e , --episode        Rename EPISODES of the series in the specified Directory
  -s , --subtitle       Rename SUBTITLES of the Series in the Directory
  -t , --tag            Rename VIDEO TAGS for MKV Videos
```

## Examples:

- Renaming all episodes in a series:

```
python rename.py -c tt000472954 -e "D:\Episode Directory" -s "D:\Subtitle Directory" -t "D:\Episode Directory"
python rename.py --code tt000472954 --episode "D:\Episode Directory" --subtitle "D:\Subtitle Directory" --tag "D:\Episode Directory"
```

- Renaming episodes upto a certain season in a series:

```
python rename.py -c tt000472954 -r 0 4 -e "D:\Episode Directory" -s "D:\Subtitle Directory" -t "D:\Episode Directory"
```

- Renaming episodes from a certain season to the end of a series:

```
python rename.py -c tt000472954 -r 4 0 -e "D:\Episode Directory" -s "D:\Subtitle Directory" -t "D:\Episode Directory"
```

- Renaming one specified season in a series:

```
python rename.py -c tt000472954 -r 4 -e "D:\Episode Directory" -s "D:\Subtitle Directory" -t "D:\Episode Directory"
```

## Running the GUI:
To run the GUI, simply run `python gui.py` in the terminal.

This GUI uses PySimpleGUI, which is a Python library for building GUI applications.

### Example Output:
- CLI:

![](https://github.com/IAmOZRules/MKVTools/blob/main/Images/example_cli.jpg)

- GUI:

<p align="center">
  <img src="https://github.com/IAmOZRules/MKVTools/blob/main/Images/example_gui.jpg" />
</p>

### NOTES:

- Individual scripts can be found [here](https://github.com/IAmOZRules/MKVTools/tree/main/Individual%20Scripts), but won't be receiving updates!
- Make sure that **ALL** episodes/subtitles are available in the one folder, not nested folders!
- Due to certain limitations not yet handled by me, ensure that the **Episodes and Subtitles are in separate folders**!

## TODO:

- [x] Convert separate scripts into a single CLI operation ✅
- [x] Add custom season/episode range to be renamed
- [ ] Renaming in nested directories
- [x] Maybe a GUI 🤷‍♂️
