import requests
import spotify
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) "
          "Gecko/20100101 Firefox/131.0"}

response = requests.get(url="https://www.billboard.com/charts/hot-100/", headers=header)

web_response = response.text

soup = BeautifulSoup(web_response, "html.parser")
billboard = soup.select("li ul li h3")
songs_name = [song.getText().strip() for song in billboard]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.org/legaz",
        client_id="c582757c4caf4ff19bccc80b4203057d",
        client_secret="cdf42fed9b964bedaad04e1f20585929",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
song_names = ["The list of song","titles from your","web scrape"]
year = date.split("-")[0]
for song in song_names:
    print(f"Searching for '{song}' from {year}...")
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    # Ensure search result contains tracks
    if result["tracks"]["items"]:
        uri = result["tracks"]["items"][0]["uri"]  # This is a URI, not a full URL
        song_uris.append(uri)
        print(f"Found URI for '{song}': {uri}")
    else:
        print(f"'{song}' doesn't exist in Spotify. Skipped.")


