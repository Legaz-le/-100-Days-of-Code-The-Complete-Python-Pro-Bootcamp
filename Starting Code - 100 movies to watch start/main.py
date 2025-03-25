import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
yc_website_page = response.text


soup = BeautifulSoup(yc_website_page, "html.parser")
films =  soup.find_all(name="h3", class_= "title")

movies_titles = [movie.getText() for movie in films]


movies = movies_titles[::-1]


with open("the best movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")


