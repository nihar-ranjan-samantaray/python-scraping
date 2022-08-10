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



def exportDF(TechnicalDataDF):

    writer = pd.ExcelWriter('technical_data.xlsx')
    TechnicalDataDF.to_excel(writer, index=False)
    writer.save()
    print("Data Scraped")
    
def scrapeTechnicalDataList(soup, tabIndex, technicalDataDF, jm_no):
    technicalDataDict = {}
    # try:
    data = soup.select('div.p_details')[0].select('div.tab_container')[tabIndex].select('div.tab_content')[0]
    technicalDataDict['JM-No.'] = jm_no
    for _ in range(1,len(data.select('tr'))):
        if data.select('tr')[_].select('td')[0].text == 'Voltage': technicalDataDict['Voltage'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Capacity': technicalDataDict['Capacity'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Pitch': technicalDataDict['Pitch'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Thread': technicalDataDict['Thread'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Length': technicalDataDict['Length'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Width': technicalDataDict['Width'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Height': technicalDataDict['Height'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Diameter': technicalDataDict['Diameter'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Weight (including acid)': technicalDataDict['Weight (including acid)'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'O-ring type': technicalDataDict['O-ring type'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Manufacturer': technicalDataDict['Manufacturer'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Type': technicalDataDict['Type'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Type1': technicalDataDict['Type1'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Type2': technicalDataDict['Type2'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Tensile strength': technicalDataDict['Tensile strength'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Colour': technicalDataDict['Colour'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Colour - Outer plates': technicalDataDict['Colour - Outer plates'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Colour - Inner plates': technicalDataDict['Colour - Inner plates'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Connection link type': technicalDataDict['Connection link type'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Product on roll': technicalDataDict['Product on roll'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Suitable for Spring Link': technicalDataDict['Suitable for Spring Link'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Suitable Solid Rivet Link': technicalDataDict['Suitable Solid Rivet Link'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Suitable Hollow Rivet Link': technicalDataDict['Suitable Hollow Rivet Link'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Inner Diameter': technicalDataDict['Inner Diameter'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Outer Diameter': technicalDataDict['Outer Diameter'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Mount': technicalDataDict['Mount'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Shaft diameter': technicalDataDict['Shaft diameter'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Total Length': technicalDataDict['Total Length'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Shaft length': technicalDataDict['Shaft length'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Activated': technicalDataDict['Activated'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Manufacturer claimed CCA': technicalDataDict['Manufacturer claimed CCA'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Manufacturers Testing Standard': technicalDataDict['Manufacturers Testing Standard'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'SAE as measured by JMP battery tester': technicalDataDict['SAE as measured by JMP battery tester'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'DIN as measured by JMP battery tester': technicalDataDict['DIN as measured by JMP battery tester'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'EN as measured by JMP battery tester': technicalDataDict['EN as measured by JMP battery tester'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Acid Pack included': technicalDataDict['Acid Pack included'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Terminal connection': technicalDataDict['Terminal connection'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Positive terminal': technicalDataDict['Positive terminal'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Negative terminal': technicalDataDict['Negative terminal'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Breather hose': technicalDataDict['Breather hose'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Negative terminal': technicalDataDict['Negative terminal'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'for thread size': technicalDataDict['for thread size'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'For bolts (dia)': technicalDataDict['For bolts (dia)'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'self-locking': technicalDataDict['self-locking'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Spanner size /SW': technicalDataDict['Spanner size SW'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Material': technicalDataDict['Material'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Surface': technicalDataDict['Surface'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Strength Classification': technicalDataDict['Strength Classification'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Grooved': technicalDataDict['Grooved'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Springs included': technicalDataDict['Springs included'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Shape': technicalDataDict['Shape'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Head': technicalDataDict['Head'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Drive Type': technicalDataDict['Drive Type'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Quality': technicalDataDict['Quality'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Gasket/Washer': technicalDataDict['Gasket/Washer'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'with bleed valve': technicalDataDict['with bleed valve'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'with brake light switch': technicalDataDict['with brake light switch'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Assortment': technicalDataDict['Assortment'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Hole for lock wire': technicalDataDict['Hole for lock wire'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()
        if data.select('tr')[_].select('td')[0].text == 'Special feature': technicalDataDict['Special feature'] = data.select('tr')[_].select('td')[1].text.replace(':','').strip()


    technicalDataDF = pd.concat([technicalDataDF, pd.DataFrame(technicalDataDict, index=[0])])
    # print(technicalDataDF)
    return technicalDataDF
    # except Exception as e:
    #     print(f"Error : ",e)

def scrapeDescription(descriptionURL, technicalDataDF):
    descriptionDict = {}
    # try:
    descriptionResponse = session.get(descriptionURL)
    soup = BeautifulSoup(descriptionResponse.content, 'lxml')
    mm_detail_container = soup.select('div.p_details')[0].select('div.mm_detail_container')
    mm_details = mm_detail_container[0].select('div.mm_details')
    descriptionDict['jm_no'] = mm_details[0].select('div.mm_drow')[0].find('div',class_='mm_right').text

    if soup.select('div.p_details')[0].select('div.tab_container') != []: 
        tab_count = len(soup.select('div.p_details')[0].select('div.tab_container'))
        tabNameList = []
        for eachTab in range(tab_count):
            tabNameList.append(soup.select('div.p_details')[0].select('div.tab_container')[eachTab].h4.text)
        
        if 'Technical data' in tabNameList:
            tabIndex = tabNameList.index('Technical data')
            technicalDataDF = scrapeTechnicalDataList(soup, tabIndex, technicalDataDF, descriptionDict['jm_no'])
        
    descriptionDict['technicalDataDataFrame'] = technicalDataDF
    return descriptionDict
    # except Exception as e:
    #     print(f"Error : ",e)

def scrapeData(url, category_count):
    
    # try:
    technicalDataDF = pd.DataFrame()
    for num in range(2010,3000,30):
        if num == 0: page = 1
        else: page = (num/30)+1
        response = session.get(f"{url}/?sr={num}")
        soup = BeautifulSoup(response.content, 'lxml')
        gallery_element = soup.select('div.gal_elem')
        print(f"Page : {int(page)}")
        
        for id,eachElement in enumerate(gallery_element):
            descriptionURL = str(eachElement.h3.a['href'])
            scrapeDescriptionData = scrapeDescription(descriptionURL, technicalDataDF)
            technicalDataDF = scrapeDescriptionData['technicalDataDataFrame']
            print("[%-30s] %d%%" % ('='*id, 3.3*(id+1)))
        exportDF(technicalDataDF)
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
    category_count = int(soup.select('div.p_alist')[0].select('table')[0].select('tr')[3].select('td')[0].text.split()[0])
    scrapeData(url, category_count)