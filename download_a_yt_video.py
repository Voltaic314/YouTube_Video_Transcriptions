'''
Author: Logan Maupin
Date: 10/24/2023

This python script just uses the pytube library to 
download a YT video for you.
'''
from pytube import YouTube
import os


def remove_special_characters_from_string(input_string: str) -> str:
    '''
    This function takes a given input string and removes all characters that aren't
    alpha-numeric or spaces. 

    Parameters:
    input_string: str you wish to format

    Returns: formatted str
    '''
    new_string = ""
    for character in input_string:
        if character.isalnum() or character.isspace():
            new_string += character
    return new_string


def get_video_url_from_user_input() -> str:
    user_input = input("Please type the YT url of the video you wish to download: ")
    if 'youtube' in user_input or 'youtu.be' in user_input:
        return user_input


def download_video(url: str, filename: str = None) -> bool:
    '''
    Saves a video to its highest resolution. Optional argument to pass in
    a custom filename. If none is passed, it will save with the video title
    as the filename, with only alphanumeric & space characters in the filename.
    '''
    video: YouTube = YouTube(url=url)
    video_filename = remove_special_characters_from_string(video.title) + ".mp4"
    
    if filename:
        video.streams.get_highest_resolution().download(filename=filename)
        return os.path.exists(filename)

    else:
        video.streams.get_highest_resolution().download(filename=video_filename)
        return os.path.exists(video_filename)
    

def main():
    video_url = get_video_url_from_user_input()
    video_was_succesfully_saved = download_video(url=video_url)

    if video_was_succesfully_saved:
        print("Video was saved successfully")

    else:
        print("There was a problem in trying to save the video...")


if __name__ == "__main__":
    main()
