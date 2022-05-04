from bs4 import BeautifulSoup
import requests
import lxml
import re

data_choice = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
# data_choice = "1985-05-04"
url = f"https://www.billboard.com/charts/hot-100/{data_choice}/"
response = requests.get(url)
# with open('file.txt', 'w') as file:
#     file.write(response.text)

# with open('file.txt', 'r') as file:
#     web_site = file.read()
# soup = BeautifulSoup(web_site, "lxml")

soup = BeautifulSoup(response.text, "lxml")

class_containers = "o-chart-results-list-row-container"
chart_results = soup.find(class_=f"{class_containers}")
# print(chart_results)
# c-label

songs_names = []
songs_labels = []
songs = soup.find_all(class_=f"{class_containers}")

for song in songs:
    chart_h3 = song.find("h3").text
    chart_h3 = re.sub(r'\n', '', chart_h3)
    chart_h3 = re.sub(r'\t', '', chart_h3)
    songs_names.append(chart_h3)
    label = (song.find_all(class_="c-label"))[1].text
    label = re.sub(r'\n', '', label)
    label = re.sub(r'\t', '', label)
    if label == "NEW":
        label = (song.find_all(class_="c-label"))[3].text
        label = re.sub(r'\n', '', label)
        label = re.sub(r'\t', '', label)
    songs_labels.append(label)

for i in range(100):
    print(f"{i+1}: {songs_names[i]} / {songs_labels[i]}")
    best_song = f"{i+1}: {songs_names[i]} / {songs_labels[i]} \n"
    with open(f'song_titles_{data_choice}.txt', 'a') as file:
        file.write(best_song)

