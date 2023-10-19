'''
Author: Logan Maupin
GitHub: https://github.com/Voltaic314
Date: 10/16/2023

The purpose of this module is to transcribe a given YT video into a 
text file given the YT url provided from user input.
'''
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter, JSONFormatter


def get_video_info(video_url) -> tuple[str, str]:
        '''
        This function takes a YT url and returns its title and video ID.

        Parameters:
        video_url: str of the YT video url

        Returns: Tuple --> (video_title, video_id)
        '''
        youtube = YouTube(video_url)
        return youtube.title, youtube.video_id, youtube.publish_date


'''
This function is generally only necessary when we are working with file formats that
don't generally support text encoding of special characters like emojis. So this is 
really just to help with barebones formatting situations.
'''
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


def format_filename_txt(video_title) -> str:
    '''
    This function takes a YT video and removes any characters that aren't alphanumeric,
    then changes spaces to underscores, and adds the .txt extension so that we can use it
    as a txt filename. 

    Parameters: 
    video_title: str of a video title you wish to format into a txt filename

    Returns: formatted str
    '''
    return remove_special_characters_from_string(video_title).replace(" ", "_") + ".txt"


def format_text_file_intro(video_title: str, video_url: str) -> str:
    """
    This function will take in a YT video object and spit out a formatted string
    with all the fancy information that we want at the top of our transcription txt file.
    
    Parameters:
    video_id: a YT video id, usually a string.
    video_title: a UTF-8 txt file friendly formatted video title string
    ideo_url: the full YT watch url string
    
    Returns: formatted string to add to the top of the transcription txt file.
    """
    text_file_header = ""
    text_file_header += f"Video Title: {video_title}\n"
    text_file_header += f"Video URL: {video_url}\n\n"

    return text_file_header


def get_text_from_video(video_id, formatter) -> str:
    '''
    This function transcribes a youtube video given a youtube video ID. 
    You can extract the video ID from the url, it's that special character
    part at the end of the url after the = sign and before any & signs.

    Parameters:
    video_id: str of video id from the YT vid you wish to transcribe

    Returns: Str of transcribed text, formatted in plain text for a text file.
    '''
    transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id)
    formatted_txt = formatter.format_transcript(transcript=transcript)
    
    return formatted_txt


def write_string_to_text_file(txt_filename: str, string_to_write: str) -> None:
    '''
    This function appends a text file with the text you wish to write to it

    Parameters: 
    txt_filename: str representing the file name of the txt file you wish to write to.
    string_to_write: str of what you wish to write to the file.

    Returns: None
    '''
    with open(txt_filename, 'a') as txt_file:
        txt_file.write(string_to_write)


def transcribe_video(video_url, formatted_type: str):
    '''
    This function transcribes a video and returns either a json string or plain text.

    Parameters:
    formatted_type: a str of the type you want this to be formatted into. Like "json" for
    json strings or "txt" for plain text.

    Returns: json str or plain text str
    '''
    video_id = get_video_info(video_url=video_url)[1]
    
    formatted_type = formatted_type.strip().lower()
    if formatted_type == "json":
        txt_from_vid = get_text_from_video(video_id=video_id, formatter=JSONFormatter())
        return txt_from_vid

    elif formatted_type == "text":
        txt_from_vid = get_text_from_video(video_id=video_id, formatter=TextFormatter())
        return txt_from_vid