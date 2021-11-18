import requests
from bs4 import BeautifulSoup
import pandas as pd


# extract(page): Means we will be Inputing the page we want into the url
def extract():

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

    # Url We Shall Be Scraping
    url = f'https://www.ooyyo.com/germany/used-cars-for-sale/c=CDA31D7114D3854F111BFE6FAA651551EDA2/'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('a', class_ = 'car-card-1')
    for item in divs:
        Make = item.find('div', class_ = 'mob-heading').text.strip()
        
        Location = item.find('div', class_ = 'mob-location').text.strip()
        Milage = item.find('div', class_ = 'mileage').text.strip().replace('\n', '')
        Description = item.find('div', class_ = 'description').text.strip().replace('\n', '')

        # Car Dictionary
        car = {
            'Make' : Make,
            'Location' : Location,
            'Milage' : Milage,
            'Description' : Description
        }

        # Appended Dictionary To Car List
        carlist.append(car)
    return

# Car List
carlist = []

c = extract()
transform(c)

df = pd.DataFrame(carlist)

print(df.head())

df.to_csv('Cars.csv')