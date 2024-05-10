import requests
import random
from collections import Counter

def fetch_powerball_data():
    # Replace the URL with the actual API URL
    url = 'https://api.powerball.com/json'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Checks for HTTP request errors
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def analyze_and_suggest_combinations(data):
    white_balls = []
    powerballs = []
    
    # Extract numbers from the data
    for drawing in data['drawings']:
        white_balls.extend(drawing['white_balls'])
        powerballs.append(drawing['powerball'])
    
    # Count the frequency of each number
    white_ball_counts = Counter(white_balls)
    powerball_counts = Counter(powerballs)
    
    # Calculate the total draws for normalization
    total_white_draws = sum(white_ball_counts.values())
    total_power_draws = sum(powerball_counts.values())
    
    # Calculate probabilities
    white_ball_probabilities = {number: count / total_white_draws for number, count in white_ball_counts.items()}
    powerball_probabilities = {number: count / total_power_draws for number, count in powerball_counts.items()}
    
    # Suggest numbers based on the highest probabilities
    suggested_white_balls = sorted(white_ball_probabilities, key=white_ball_probabilities.get, reverse=True)[:5]
    suggested_powerball = sorted(powerball_probabilities, key=powerball_probabilities.get, reverse=True)[0]
    
    return suggested_white_balls, suggested_powerball

# Main Execution
data = fetch_powerball_data()
if data:
    suggested_white_balls, suggested_powerball = analyze_and_suggest_combinations(data)
    print(f"Suggested White Balls: {suggested_white_balls}")
    print(f"Suggested Powerball: {suggested_powerball}")
else:
    print("Failed to fetch or analyze Powerball data.")
