from bs4 import BeautifulSoup
import requests
import lxml
import re

data_choice = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{data_choice}/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

class_containers = "o-chart-results-list-row-container"
chart_results = soup.find(class_=f"{class_containers}")

def clean_string(item):
    clean = re.sub(r'\n', '', item)
    return re.sub(r'\t', '', clean)

songs_names = []
songs_labels = []
songs = soup.find_all(class_=f"{class_containers}")

for song in songs:

    chart_h3 = song.find("h3").text
    songs_names.append(clean_string(chart_h3))

    label = (song.find_all(class_="c-label"))[1].text
    if clean_string(label) == "NEW":
        label = (song.find_all(class_="c-label"))[3].text
    songs_labels.append(clean_string(label))

for i in range(100):
    print(f"{i+1}: {songs_names[i]} / {songs_labels[i]}")
    best_song = f"{i+1}: {songs_names[i]} / {songs_labels[i]} \n"
    with open(f'song_titles_{data_choice}.txt', 'a') as file:
        file.write(best_song)

