import requests
import random
from collections import Counter

def fetch_powerball_data():
    # Replace the URL with the actual API URL
    url = 'https://api.powerball.com/json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def analyze_frequencies(data):
    white_balls = []
    powerballs = []
    
    for drawing in data['drawings']:
        white_balls.extend(drawing['white_balls'])
        powerballs.append(drawing['powerball'])
    
    white_ball_counts = Counter(white_balls)
    powerball_counts = Counter(powerballs)
    
    total_white_draws = sum(white_ball_counts.values())
    total_power_draws = sum(powerball_counts.values())
    
    white_ball_probabilities = {number: count / total_white_draws for number, count in white_ball_counts.items()}
    powerball_probabilities = {number: count / total_power_draws for number, count in powerball_counts.items()}
    
    return white_ball_probabilities, powerball_probabilities

def suggest_combination(white_ball_probs, powerball_probs):
    # Sort numbers by probability and pick top 5 for white balls and top 1 for powerball
    white_balls = sorted(white_ball_probs, key=white_ball_probs.get, reverse=True)[:5]
    powerball = sorted(powerball_probs, key=powerball_probs.get, reverse=True)[0]
    
    return white_balls, powerball

# Main Execution
data = fetch_powerball_data()
if data:
    white_ball_probs, powerball_probs = analyze_frequencies(data)
    suggested_white_balls, suggested_powerball = suggest_combination(white_ball_probs, powerball_probs)
    print(f"Suggested White Balls: {suggested_white_balls}")
    print(f"Suggested Powerball: {suggested_powerball}")
else:
    print("Failed to fetch or analyze Powerball data.")
