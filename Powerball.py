import random
import json
import sys

def generate_powerball_numbers():
    white_balls = random.sample(range(1, 70), 5)
    powerball = random.randint(1, 26)
    return sorted(white_balls) + [powerball]

result = generate_powerball_numbers()
print(json.dumps(result))  # Print the result as a JSON string for Node.js to read
sys.stdout.flush()  # Ensure all output is flushed to the buffer
