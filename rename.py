import os
import imdb
import argparse
from termcolor import colored

'''
Arguments for the script

    -c, --code      : IMDb Code
    -r, --range     : Season range for rename
    -e, --episode   : Directory to rename the episodes
    -s, --subtitle  : Directory to rename the subtitles
    -t, --tag       : Directory to edit the tags
'''

arg_parser = argparse.ArgumentParser(usage='python rename.py [-h] [options]')
arg_parser.add_argument('-c', '--code', type=str, help='IMDb CODE for the Series', required=False, metavar='')
arg_parser.add_argument('-r', '--range', type=int, nargs="+", help='Season range for rename', required=False, metavar='', default=[0,0])
arg_parser.add_argument('-e', '--episode', type=str, help='Rename EPISODES of the series in the specified Directory', default=False, metavar='')
arg_parser.add_argument('-s', '--subtitle', type=str, help='Rename SUBTITLES of the Series in the Directory', default=False, metavar='')
arg_parser.add_argument('-t', '--tag', type=str, help='Rename VIDEO TAGS for MKV Videos', required=False, metavar='')

args = arg_parser.parse_args()

not_allowed = r":\*<>\|"

def get_episodes(imdb_code, start=0, end=0):
    """
    Function to get Episode List from IMDb using the IMDb Code

    Parameters
    ----------
    imdb_code : str
        IMDb Code for the Series
    start : int
        Season range for rename
    end : int
        Season range for rename

    Returns
    -------
    episode_list : list
        List of episodes to be renamed
    """

    ia = imdb.IMDb()
    if "tt" in imdb_code: imdb_code = imdb_code[2:]

    series = ia.get_movie(imdb_code)
    print("\nSERIES: {}".format(colored(series, "magenta")))

    ia.update(series, "episodes")
    episodes = series.data['episodes']

    episode_list = []

    seasons_list = []
    if start == 0 and end == 0:
        seasons_list = [i for i in range(1, len(episodes)+1)]
    elif start != 0 and end == 0:
        seasons_list = [i for i in range(start, len(episodes)+1)]
    elif start == 0 and end != 0:
        seasons_list = [i for i in range(1, end+1)]
    else:
        seasons_list = [i for i in range(start, end+1)]

    print("SEASONS: {}\n".format(colored(seasons_list, "magenta")))

    for season in seasons_list:
        for episode in episodes[season]:
            title = episodes[season][episode]['title']

            if season < 10:
                if episode < 10:
                    ep_name = "{} S0{}E0{} - {}".format(series, season, episode, title)
                else:
                    ep_name = "{} S0{}E{} - {}".format(series, season, episode, title)
            else:
                if episode < 10:
                    ep_name = "{} S{}E0{} - {}".format(series, season, episode, title)
                else:
                    ep_name = "{} S{}E{} - {}".format(series, season, episode, title)
            
            for i in ep_name:
                if i in not_allowed:
                    ep_name = ep_name.replace(i, " -")
                if i in "\/":
                    ep_name = ep_name.replace(i, "-")
                if i in "?":
                    ep_name = ep_name.replace(i, "")
            episode_list.append(ep_name)
    
    return episode_list

def rename_episode(directory, episode_list):
    """
    Function to rename the episodes in the specified directory

    Parameters
    ----------
    directory : str
        Directory to rename the episodes
    episode_list : list[str]
        List of episodes to be renamed    
    """

    files = os.listdir(directory)
    print("Renaming episodes...")

    for i in range(len(files)):
        ep_name = episode_list[i]
        og_name = files[i]
        ext = og_name[-4:]
        if ext != ".srt":
            ep_name += ext
            filename = os.path.join(directory, og_name)
            newfilename = os.path.join(directory, ep_name)
            print("Renaming {} to {}".format(colored(filename, 'yellow'), colored(newfilename, 'green')))
            os.rename(filename, newfilename)
    print(colored("RENAMING", "red"), colored("EPISODES", "cyan"), colored("FINISHED!\n", "red"))

def rename_subtitle(directory, episode_list):
    """
    Function to rename the subtitles in the specified directory

    Parameters
    ----------
    directory : str
        Directory to rename the subtitles
    episode_list : list[str]
        List of episodes to be renamed
    """

    files = os.listdir(directory)
    print("Renaming subtitles...")

    for i in range(len(files)):
        ep_name = episode_list[i]
        og_name = files[i]
        ext = og_name[-4:]
        if ext == ".srt":
            ep_name += ext
            filename = os.path.join(directory, og_name)
            newfilename = os.path.join(directory, ep_name)
            print("Renaming {} to {}".format(colored(filename, 'yellow'), colored(newfilename, 'green')))
            os.rename(filename, newfilename)
    print(colored("RENAMING", "red"), colored("SUBTITLES", "cyan"), colored("FINISHED!\n", "red"))

def edit_tag(directory):
    """
    Function to edit tags of the MKV files to their file name in the specified directory

    Parameters
    ----------
    directory : str
        Directory to edit the tags
    """

    for file in os.listdir(directory):
        if ".mkv" in file:
            title = file.replace(".mkv", "")
        
        if ".mp4" in file:
            title = file.replace(".mp4", "")

        command = r'mkvpropedit "{}\{}" --set "title={}"'.format(directory, file, title)
        os.system(command)
        
    print(colored("RENAMING", "red"), colored("VIDEO TAGS", "cyan"), colored("FINISHED!\n", "red"))

if __name__ == "__main__":
    if args.range:
        if len(args.range) == 2:
            start, end = args.range[0], args.range[1]
        else:
            start = end = args.range[0]
    else:
        start, end = 0, 0

    if args.code:
        episodes = get_episodes(args.code, start, end)

    if args.episode:
        args.episode = r'{}'.format(args.episode)
        rename_episode(args.episode, episodes)
    
    if args.subtitle:
        args.subtitle = r'{}'.format(args.subtitle)
        rename_subtitle(args.subtitle, episodes)
    
    if args.tag:
        args.tag = r'{}'.format(args.tag)
        edit_tag(args.tag)