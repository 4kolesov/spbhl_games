import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import lxml
from fake_useragent import UserAgent

user = UserAgent().random


headers = {
    'user-agent': user
}
URL = 'http://spbhl.ru/Team?TournamentID=5862&TeamID=2707eeb5-1b8f-4128-b5ca-57e8d8d8ace0'
# URL = 'https://browser-info.ru/'

# response = requests.get(URL)
response = requests.get(URL, headers=headers).text

soup = bs(response, 'lxml')
# block = soup.find('div', class_='scoresribbon').text
games = soup.find('div', class_='scoresribbon')

# game = games.find('div', id='match')
# date = game.find('th', class_='date').find('span', id='DL').text
# time = game.find('th', class_='time').find_all('span')[0].text
# game_link = game.find('td', colspan='2').find('a', href=True)['href']
# arena_link = game.find('td', class_='icons').find('a', id='AHL', href=True)['href']
# team_guest = game.find_all('td', class_='team')[0].text
# team_guest_score = game.find_all('td', class_='score')[0].text
# team_home = game.find_all('td', class_='team')[1].text
# team_home_score = game.find_all('td', class_='score')[1].text



# print(
#     f'{date} {time}\n'
#     f'Матч: {game_link}\n'
#     f'Арена: {arena_link}\n'
#     f'{team_guest} {team_guest_score} : {team_home_score} {team_home}\n'
# )


for game in games.find_all('div', id='match'):
    date = game.find('th', class_='date').find('span', id='DL').text
    time = game.find('th', class_='time').find_all('span')[0].text
    game_link = game.find('td', colspan='2').find('a', href=True)['href']
    arena_link = game.find('td', class_='icons').find('a', id='AHL', href=True)['href']
    arena_name = game.find('td', class_='icons').find('a', id='AHL', title=True)['title']
    team_guest = game.find_all('td', class_='team')[0].text
    team_guest_score = game.find_all('td', class_='score')[0].text
    team_home = game.find_all('td', class_='team')[1].text
    team_home_score = game.find_all('td', class_='score')[1].text

    print(
        f'{date} {time} {arena_name}\n'
        f'{team_guest} [{team_guest_score} : {team_home_score}] {team_home}\n'
        f'Ссылка на матч: http://spbhl.ru/{game_link}\n'
        f'Ссылка на арену: http://spbhl.ru/{arena_link}\n'
    )
