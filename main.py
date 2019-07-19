from bs4 import BeautifulSoup as bs

def readfile(path='./index.html'):
    with open(path, 'r', encoding='utf-8') as infile:
        data = infile.read()
        return data


def extract_br(html: str):
    souped = bs(html, 'lxml')

    for row in souped.find_all('tr', attrs={'class': ['row1', 'row2']}):
	    a = row.find_next('td').find_next('td').find_next('td')
	    sxoli = a.parent.find('a').text
	    #print(sxoli)

	    city = a.find_next('td').find('a').text
	    #print(city)

	    moria = row.find('td', attrs={'class': 'vaseis'}).text
	    #print(moria)

	    l = ','.join([sxoli, city, moria])
	    print (l)


if __name__ == "__main__":
    h = readfile()
    extract_br(h)
