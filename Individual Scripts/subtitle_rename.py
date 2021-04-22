import os
import sys
import imdb

print("Searching Series Name...")
ia = imdb.IMDb()
code = "3032476"
series = ia.get_movie(code)

ia.update(series, "episodes")
episodes = series.data['episodes']
directory = r"D:\Torrents\Subs"

episode_list = []

print("Creating list of episode names...")
for season in episodes.keys():
    for episode in episodes[season]:
        title = episodes[season][episode]['title']

        if episode < 10:
            ep_name = "{} S0{}E0{} - {}.srt".format(series, season, episode, title)
        else:
            ep_name = "{} S0{}E{} - {}.srt".format(series, season, episode, title)
        
        episode_list.append(ep_name)

files = os.listdir(directory)

print("Renaming episodes...")
for i in range(len(files)):
    ep_name = episode_list[i]
    if ".srt" in ep_name:
        og_name = files[i]
        filename = os.path.join(directory, og_name)
        newfilename = os.path.join(directory, ep_name)
        os.rename(filename, newfilename)

print("renaming done")