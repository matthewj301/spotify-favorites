import spotipy
from spotipy.oauth2 import SpotifyOAuth


class FavoriteMusicFinder:
    def __init__(self, config):
        self.config = config
        self.spotify_client_id = self.config['spotify']['client_id']
        self.spotify_client_secret = self.config['spotify']['client_secret']
        self.spotify_redirect_url = self.config['spotify']['redirect_url']
        self.favorite_artists = []
        self.favorite_generes = []
        self.scope = 'user-top-read'
        self.find_music()

    def find_music(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.spotify_client_id,
                                                       client_secret=self.spotify_client_secret,
                                                       redirect_uri=self.spotify_redirect_url, scope=self.scope)
                             )

        results = sp.current_user_top_artists()['items']
        for _artist in results:
            self.favorite_generes += _artist['genres']
            self.favorite_artists.append(_artist['name'])
