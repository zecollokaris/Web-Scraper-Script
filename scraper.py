import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse
from selenium import webdriver

# Import urls From Url File
from urls import urls

# extract(page): Means we will be Inputing the page we want into the url
def extract(url):

    # Url Instance Is Parsed
    r = requests.get(url, {})
    # Creates An Instance Of Beautiful Soup & Initialize
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    # Finding a tag (<a> </a>) with class (car-card-1) In Initialized Instance
    divs = soup.find_all('a', class_ = 'car-card-1')

    # Looping Is Done To Find Contents Found Inside a tag (<a> </a>)
    for item in divs:
        # Looping Trough a tag contents and we strip the data inside the div's
        Make = item.find('div', class_ = 'mob-heading').text.strip()
        Price = item.find('div', class_ = 'price-info').text.strip()
        Location = item.find('div', class_ = 'mob-location').text.strip()
        Milage = item.find('div', class_ = 'mileage').text.strip().replace('\n', '')
        Description = item.find('div', class_ = 'description').text.strip().replace('\n', '')
        Link = driver.find_element_by_xpath('a', class_ = 'car-card-1').click()

        # Car 
        car = {
            'Make' : Make,
            'Price' : Price,
            'Location' : Location,
            'Milage' : Milage,
            'Description' : Description,
            'Link' : Link
        }

        # Appended To Car List
        carlist.append(car)
    return


def parseUrl(url):
    c = extract(url)
    transform(c)
    # Return Data In A Tubular Manner (Rows & Columns)
    df = pd.DataFrame(carlist)
    # Data Is Stored In a Csv File
    df.to_csv('Cars.csv')

# Car List
carlist = []

# Get Args Parsed Inside Script
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('string', metavar='N', type=str, nargs='+',
                    help='an integer for the accumulator')
args = parser.parse_args()

# Filter String From Urls Array 
filter_object = filter(lambda a: args.string[0] in a, urls)

parseUrl(list(filter_object)[0])



