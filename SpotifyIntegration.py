from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
load_dotenv()
client_credentials_manager = SpotifyClientCredentials(client_id=os.environ["spotipy_cid"], client_secret=os.environ.get["spotipy_sec"])
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def skip():
    spotipy.next_track()

def prev():
    spotipy.previous_track()

def pause():
    spotipy.pause_playback()

def play():
    spotipy.start_playback()

def shuffle(state):
    spotipy.shuffle(state)

def search_song(message):
    song = spotipy.search(message, 10, 0, 'track')
    spotipy.add_to_queue(song.items[0])

def how_to_search():
    return "Filters:\n\tgenre\n\talbum\n\tartist\n\ttrack\n\tyear\n\ttag:hipster\n\ttag:new\n\t"
