from fastapi import FastAPI
from spotify_favorites.favorite_music_finder import FavoriteMusicFinder
import yaml
from pathlib import Path


config_file = Path(__file__).resolve().parent.parent.joinpath('etc/config.yaml')
config = yaml.safe_load(open(config_file))
f_music = FavoriteMusicFinder(config)

app = FastAPI()


@app.get("/personal/music/artists")
async def get_favorite_artists():
    return {"favorite_artists": f_music.favorite_artists}


@app.get("/personal/music/genres")
async def get_favorite_genres():
    return {"favorite_genres": f_music.favorite_generes}