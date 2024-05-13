import requests
from bs4 import BeautifulSoup
import json

# URL of the Powerball results page
url = 'https://www.powerball.com/games/home'

def get_powerball_data():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize data storage
    data = {
        'winning_combinations': [],
        'jackpots_won': [],
        'next_drawing': '',
        'next_jackpot': ''
    }

    # Scrape winning combinations and jackpots won
    for draw in soup.select('.winning-numbers .results-draw-date'):
        date = draw.text.strip()
        numbers = draw.find_next('ul').text.strip()
        jackpot = draw.find_next('span', class_='jackpot-amount').text.strip()
        data['winning_combinations'].append({
            'date': date,
            'numbers': numbers,
            'jackpot': jackpot
        })
    
    # Scrape next drawing and jackpot info
    next_drawing_info = soup.find('div', class_='next-drawing')
    if next_drawing_info:
        data['next_drawing'] = next_drawing_info.find('span', class_='draw-date').text.strip()
        data['next_jackpot'] = next_drawing_info.find('span', class_='jackpot-amount').text.strip()

    return data

# Fetch and print Powerball data
powerball_data = get_powerball_data()
print(json.dumps(powerball_data, indent=2))
