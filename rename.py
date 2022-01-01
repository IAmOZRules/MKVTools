from func import *
import argparse

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

if __name__ == "__main__":
    if args.range:
        if len(args.range) == 2:
            start, end = args.range[0], args.range[1]
        else:
            start = end = args.range[0]
    else:
        start, end = 0, 0

    if args.code:
        _, _, episodes = get_episodes(args.code, start, end, verbose=True)

    if args.episode:
        args.episode = r'{}'.format(args.episode)
        rename_episode(args.episode, episodes, verbose=True)
    
    if args.subtitle:
        args.subtitle = r'{}'.format(args.subtitle)
        rename_subtitle(args.subtitle, episodes, verbose=True)
    
    if args.tag:
        args.tag = r'{}'.format(args.tag)
        edit_tag(args.tag, verbose=True)