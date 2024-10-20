import requests
from bs4 import BeautifulSoup
import time

def scrape_halal_stocks():
    base_url = "https://halalstock.in/halal-shariah-compliant-shares-list/"
    page = 1
    halal_stocks = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }

    print("scrapping table....")

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve page {page}. Error: {e}")
        
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='tablepress')
    
    if not table:
        print(f"No table found on page {page}. Stopping.")
        
    rows = table.find_all('tr')
    found_stocks = False
    for row in rows[1:]:  # Skip header row
        columns = row.find_all('td')
        if len(columns) >= 3:
            name = columns[1].text.strip()
            status_img = columns[0].find('img')
            if status_img and 'hs-yes.jpg' in status_img.get('src', ''):
                halal_stocks.append(name)

    return halal_stocks
