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

    Returns: str - copy of input string with only its letters, numbers, and spaces.
    '''
    new_string = ""
    for character in input_string:
        if character.isalnum() or character.isspace():
            new_string += character
    return new_string


def get_video_url_from_user_input() -> str:
    '''
    This function asks the user for input to get the YT url that we want to download.

    Returns: str representation of the YT url they want to download.
    '''
    while True:
        user_input = input("Please type the YT url of the video you wish to download: ").strip()
        
        # make sure user gave a valid YT link
        if 'youtube' in user_input or 'youtu.be' in user_input:
            return user_input
        
        else:
            print("I don't understand that link. Please enter only the link of the video with a youtube.com or youtu.be url...")


def download_video(url: str, filename: str = None) -> bool:
    '''
    Saves a video to its highest resolution. Optional argument to pass in
    a custom filename. If none is passed, it will save with the video title
    as the filename, with only alphanumeric & space characters in the filename.
    
    Parameters: 
    url: the string of the URL of the YT vid you want to download. 
    This can be a normal url like youtube.com, or shortened like youtu.be, and
    this also works for shorts and past livestreams. 
    filename: str of the filename you wish to use. Can be relative or absolute.

    Returns: True if the file was successfully saved, False otherwise.
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
