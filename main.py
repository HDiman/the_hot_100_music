from bs4 import BeautifulSoup
import requests
import lxml
import re

# data_choice = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
# data_choice = "1985-05-04"
# url = f"https://www.billboard.com/charts/hot-100/{data_choice}/"
# response = requests.get(url)
# with open('file.txt', 'w') as file:
#     file.write(response.text)

with open('file.txt', 'r') as file:
    web_site = file.read()
soup = BeautifulSoup(web_site, "lxml")

containers = "o-chart-results-list-row-container"
# chart_results = soup.find(class_=f"{class_container}")
# print(chart_results)

song_names = []
chart_h3 = soup.find(class_=f"{containers}").find("h3").text
chart_h3 = re.sub(r'\n', '', chart_h3)
chart_h3 = re.sub(r'\t', '', chart_h3)
song_names.append(chart_h3)

print(song_names)
# string = string.replace('\n',"")
# string = string.replace('\t',"")

