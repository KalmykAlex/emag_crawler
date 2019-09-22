import csv
import os.path
import requests
from datetime import datetime
from bs4 import BeautifulSoup


def get_total_pages_number(link):
    contents = requests.get(link).content
    soup = BeautifulSoup(contents, 'html.parser')
    return int(soup.findAll('a', {'class': 'js-change-page hidden-xs hidden-sm'})[-1].get_text())


def link_former(link, page_number=1):
    return link[:-2] + '/p' + str(page_number) + link[-2:]


if __name__ == '__main__':
    links = ['https://www.emag.ro/televizoare/c',
             'https://www.emag.ro/scaune-gaming/c',
             'https://www.emag.ro/laptopuri/c',
             'https://www.emag.ro/telefoane-mobile/c',
             'https://www.emag.ro/monitoare-lcd-led/c'
             ]
    date = datetime.now().strftime('%Y-%m-%d')

    for link in links:
        num_of_pages = get_total_pages_number(link_former(link))
        csvfilename = f"echipamente//{link.split('/')[-2]}//{date}.csv"

        if not os.path.isfile(csvfilename):

            for page_number in range(1, num_of_pages+1):
                contents = requests.get(link_former(link, page_number)).content
                soup = BeautifulSoup(contents, 'html.parser')

                items = soup.findAll('div', {'class': 'card-section-wrapper js-section-wrapper'})

                for item in items:
                    product_link = item.find('a', {'class': 'product-title js-product-url'}).get('href')
                    product_price = item.find('p', {'class': 'product-new-price'}).get_text().replace('.', '')[:-6]

                    with open(csvfilename, 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([product_link, product_price])

                print(f'Page {page_number}/{num_of_pages}')
        else:
            print('CSV file already created')
        print(f'Done! {csvfilename}')
