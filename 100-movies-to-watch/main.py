import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movies]
# reversing the list
movie_titles = movie_titles[::-1] # alternatively, movie_titles.reverse()

with open(r"./100-movies-to-watch/movies.txt", mode="w", encoding="utf8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
        
# with open("movies.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)