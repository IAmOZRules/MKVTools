import os
import imdb
from termcolor import colored

not_allowed = r":\*<>\|"

def get_episodes(imdb_code, start=0, end=0, verbose=False):
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
    verbose : bool
        Verbose mode

    Returns
    -------
    series: str
        Series Name
    seasons_list: list[str]
        List of Seasons
    episode_list: list[str]
        List of Episodes
    """

    ia = imdb.IMDb()
    if "tt" in imdb_code: imdb_code = imdb_code[2:]

    series = ia.get_movie(imdb_code)

    if verbose:
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

    if verbose:
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
    
    return series, seasons_list, episode_list

def rename_episode(directory, episode_list, verbose=False):
    """
    Function to rename the episodes in the specified directory

    Parameters
    ----------
    directory : str
        Directory to rename the episodes
    episode_list : list[str]
        List of episodes to be renamed    
    verbose : bool
        Verbose mode
    """

    files = os.listdir(directory)

    if verbose:
        print("Renaming episodes...")

    for i in range(len(files)):
        ep_name = episode_list[i]
        og_name = files[i]
        ext = og_name[-4:]
        if ext != ".srt":
            ep_name += ext
            filename = os.path.join(directory, og_name)
            newfilename = os.path.join(directory, ep_name)

            if verbose:
                print("Renaming {} to {}".format(colored(filename, 'yellow'), colored(newfilename, 'green')))
            os.rename(filename, newfilename)
    
    if verbose:
        print(colored("RENAMING", "red"), colored("EPISODES", "cyan"), colored("FINISHED!\n", "red"))

def rename_subtitle(directory, episode_list, verbose=False):
    """
    Function to rename the subtitles in the specified directory

    Parameters
    ----------
    directory : str
        Directory to rename the subtitles
    episode_list : list[str]
        List of episodes to be renamed
    verbose : bool
        Verbose mode
    """

    files = os.listdir(directory)

    if verbose: print("Renaming subtitles...")

    for i in range(len(files)):
        ep_name = episode_list[i]
        og_name = files[i]
        ext = og_name[-4:]
        if ext == ".srt":
            ep_name += ext
            filename = os.path.join(directory, og_name)
            newfilename = os.path.join(directory, ep_name)
            
            if verbose:
                print("Renaming {} to {}".format(colored(filename, 'yellow'), colored(newfilename, 'green')))
            os.rename(filename, newfilename)
    
    if verbose:
        print(colored("RENAMING", "red"), colored("SUBTITLES", "cyan"), colored("FINISHED!\n", "red"))

def edit_tag(directory, verbose=False):
    """
    Function to edit tags of the MKV files to their file name in the specified directory

    Parameters
    ----------
    directory : str
        Directory to edit the tags
    verbose : bool
        Verbose mode
    """

    for file in os.listdir(directory):
        if ".mkv" in file:
            title = file.replace(".mkv", "")
        
        if ".mp4" in file:
            title = file.replace(".mp4", "")

        command = r'mkvpropedit "{}\{}" --set "title={}"'.format(directory, file, title)
        os.system(command)

    if verbose:    
        print(colored("RENAMING", "red"), colored("VIDEO TAGS", "cyan"), colored("FINISHED!\n", "red"))