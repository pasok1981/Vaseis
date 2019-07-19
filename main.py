import csv
import requests

from bs4 import BeautifulSoup as bs


def readfile(path='./index.html'):
    with open(path, 'r', encoding='utf-8') as infile:
        data = infile.read()
        return data


def extract_br(html: str):
    souped = bs(html, 'lxml')

    for row in souped.find_all('tr', attrs={'class': ['row1', 'row2']}):
        a = row.find_next('td').find_next('td').find_next('td')
        sxoli = a.parent.find('a').text.replace(',', '')
        # print(sxoli)

        city = a.find_next('td').find('a').text
        # print(city)

        moria = row.find('td', attrs={'class': 'vaseis'}).text
        # print(moria)

        l = ','.join([sxoli, city, moria])
        print(l)

        csv.register_dialect('md',
                             delimiter=',',
                             quoting=csv.QUOTE_NONE,
                             skipinitialspace=True)

        with open('data.csv', mode='a', encoding='utf-8') as out:
            csv_writer = csv.writer(
                out, dialect='md')
            csv_writer.writerow([sxoli, city, moria])


if __name__ == "__main__":
    # h = readfile()
   
    year, pedio = 2017, 4
    url = f"https://aeitei.gr/index.php?year={year}&pedio={pedio}"
    req = requests.get(
        url, headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"})
    
    extract_br(req.text)
