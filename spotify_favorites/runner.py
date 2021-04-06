from spotify_favorites.favorite_music_finder import FavoriteMusicFinder
import yaml
from pathlib import Path
import time

config_file = Path(__file__).resolve().parent.parent.joinpath('etc/config.yaml')
config = yaml.safe_load(open(config_file))
f_music = FavoriteMusicFinder(config)


while True:
    f_music.find_music()
    time.sleep(86400)