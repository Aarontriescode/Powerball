Powerball Data Scraper and Server
Project Overview
This project scrapes Powerball lottery data from the official Powerball website and serves it via a Node.js server. The data includes winning combinations, jackpots, and information about the next drawing.

Features
Scrapes current and historical Powerball data.
Serves scraped data through a web interface.
Displays next drawing information and historical winning combinations.
Directory Structure
powerball-app/
├── public/
│   └── index.html
├── script.py
├── server.js
├── package.json
└── package-lock.json

Prerequisites
Node.js
Python 3.x
pip (Python package installer)

Installation
Clone the repository:
git clone <repository_url>
Install Node.js dependencies:
Install Python dependencies:
pip install requests beautifulsoup4

Running the Application
Start the Node.js server:
Open a web browser and navigate to http://localhost:3000.

Usage
Click the "Fetch Data" button on the web page to scrape and display Powerball data.
The page will display the next drawing information and historical winning combinations.
File Descriptions
script.py: Python script for web scraping Powerball data.
server.js: Node.js server script that executes the Python script and serves the data.
public/index.html: HTML file providing the frontend interface.
Detailed Explanation
script.py
This Python script uses the requests library to fetch HTML content from the Powerball website and BeautifulSoup to parse the HTML and extract relevant data. The data is then formatted as JSON and printed to the console.

server.js
This Node.js script sets up an Express server. It includes an endpoint /scrape that runs the Python script using python-shell, parses the script's JSON output, and sends it to the client. The server also serves static files from the public directory.

index.html
The HTML file includes a button that, when clicked, sends a request to the /scrape endpoint to fetch the latest Powerball data. The data is then displayed on the page.

License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

Contribution
If you want to contribute to this project, please fork the repository and submit a pull request with your improvements.

Contact
For any questions or suggestions, please contact [Aaron] at [aaron.sochor@outlook.com].
