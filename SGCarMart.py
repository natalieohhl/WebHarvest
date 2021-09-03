from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.sgcarmart.com/new_cars/index.php" 

try:
    page = urlopen(url)
    print("Page opened successfully")
    soup = BeautifulSoup(page, "html.parser")

    raw_data = soup.findAll("div", {"class": "limittwolines"})
    print(raw_data)

    new_cars = []

    for html_element in raw_data:
        new_cars.append(html_element.text)

    new_cars.sort()

    for index, car in enumerate(new_cars):
        print("{:3} ) {}".format(index+1,car))

except Exception as exception:
    print(exception)
