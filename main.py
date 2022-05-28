import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

result = requests.get(url=URL).text

soup = BeautifulSoup(result, "html.parser")

h3_tags = soup.find_all(name="h3", class_="title")

list_of_titles = [title.getText() for title in h3_tags][::-1]
print(list_of_titles)

with open("data.txt", "w") as file:
    file.write("\n".join(i for i in list_of_titles))