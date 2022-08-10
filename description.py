import requests
from bs4 import BeautifulSoup
import pandas as pd

payload = {
    'mcustno': '3036','mpassword': '175193',
    'smbtn': 'Login','lang': 'en','faction': 'login',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5','Origin': 'https://www.larsson.uk.com','Connection': 'keep-alive',
    'Referer': 'https://www.larsson.uk.com/','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-site','Sec-Fetch-User': '?1',
}

session = requests.Session()

connect = session.post('https://mike.larsson.uk.com/en/', headers=headers, data=payload)



def exportDF(scrapingData):
    
    data = pd.DataFrame(scrapingData)
    writer = pd.ExcelWriter('description.xlsx')
    data.to_excel(writer, index=False)
    writer.save()
    print("Data Scraped")
   
def scrapeDescription(descriptionURL):
    descriptionDict = {}
    # try:
    descriptionResponse = session.get(descriptionURL)
    soup = BeautifulSoup(descriptionResponse.content, 'lxml')
    if soup.select('div.p_details')[0].select('div.tab_container') == []: 
        descriptionDict['description'] = ''
    else:
        if soup.select('div.p_details')[0].select('div.tab_container')[0].h4.text == 'Description':
            description_list = soup.select('div.p_details')[0].select('div.tab_container')[0].select('div.goog_trans_cont')[0].select('div.goog_trans_res')[0].select('p')
            descriptionDict['description'] = ' '.join([each_description.text.replace(u'\xa0','') for each_description in description_list])
        else:
            print("Description Blank")
            descriptionDict['description'] = ''

    return descriptionDict
    # except Exception as e:
    #     print(f"Error : ",e)

def scrapeData(url):
    
    description_list = []
    # try:
    for num in range(3000,6000,30):
        if num == 0: page = 1
        else: page = (num/30)+1
        response = session.get(f"{url}/?sr={num}")
        soup = BeautifulSoup(response.content, 'lxml')
        gallery_element = soup.select('div.gal_elem')
        print(f"Page : {int(page)}")
        for id,eachElement in enumerate(gallery_element):
            descriptionURL = str(eachElement.h3.a['href'])
            scrapeDescriptionData = scrapeDescription(descriptionURL)
            description_list.append(scrapeDescriptionData['description'])
            print("[%-30s] %d%%" % ('='*id, 3.3*(id+1)))
        scrapingData = {
            'Description': description_list
        }
        exportDF(scrapingData)
    # except Exception as e:
    #     print(f"Error : ",e)
        
    
    
if __name__=='__main__':
    # url = 'https://mike.larsson.uk.com/en/ta/22/category/10108010000'
    # url = 'https://mike.larsson.uk.com/en/category/10109000000'
    # url = 'https://mike.larsson.uk.com/en/category/10320000000'
    # url = 'https://mike.larsson.uk.com/en/category/10409030300/'
    url = 'https://mike.larsson.uk.com/en/category/10700000000/'
    # url = 'https://mike.larsson.uk.com/en/category/10304020000/'

    response = session.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    scrapeData(url)