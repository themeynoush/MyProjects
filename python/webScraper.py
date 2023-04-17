# Build a simple web scraper that extracts information from a website and saves it to a file or database.
import requests
from bs4 import BeautifulSoup
import csv

# Define the URL to scrape
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

# Send a GET request to the URL and store the response
response = requests.get(url)

# Parse the HTML content using BeautifulSoup    
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the country population data
table = soup.find('table', {'class': 'wikitable'})

# Extract the table headers and rows
headers = [header.text.strip() for header in table.find_all('th')]
rows = []
for row in table.find_all('tr')[1:]:
    cells = [cell.text.strip() for cell in row.find_all('td')]
    rows.append(cells)

# Write the data to a CSV file
with open('country_population.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)
