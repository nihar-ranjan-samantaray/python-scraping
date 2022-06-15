import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://mike.larsson.uk.com/en/category/10320040000/?sr=240'
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


def scrapeDescription(descriptionURL, fitsToDF):
    descriptionDict = {}
    fitsToDict = {}
    descriptionResponse = session.get(descriptionURL)
    soup = BeautifulSoup(descriptionResponse.content, 'lxml')
    mm_details = soup.select('div.p_details')[0].select('div')[0].select('div.mm_details')
    mm_images = soup.select('div.p_details')[0].select('div')[0].select('div.mm_images')[0].select('div.mm_images_box')[0].select('a')[0]['href'].replace('//','https://')
    descriptionDict['jm_no'] = mm_details[0].select('div.mm_drow')[0].find('div',class_='mm_right').text
    descriptionDict['quantity'] = int(mm_details[0].select('div.mm_drow')[3].find('div',class_='mm_right').text[:1])
    descriptionDict['purchase_price'] = mm_details[0].select('div.mm_drow')[7].find('div',class_='mm_right').text[2:]
    descriptionDict['retail_price'] = mm_details[0].select('div.mm_drow')[4].find('div',class_='mm_right').text[2:6]
    descriptionDict['image'] = mm_images
    # DATA = p_details[0].select('div.mm_drow')[1].find('div',class_='mm_right').text[2:]
    description_list = soup.select('div.p_details')[0].select('div.tab_container')[0].select('div.goog_trans_cont')[0].select('div.goog_trans_res')[0].select('p')[3:]
    descriptionDict['description'] = ' '.join([each_description.text[1:-1].replace(u'\xa0','') for each_description in description_list])
    print(soup.select('div.p_details')[0].select('div.tab_container')[1].select('div.tab_content')[0])
    tdaDetails = soup.select('div.p_details')[0].select('div.tab_container')[1].select('div.tab_content')[0].select('div.related_articles')[0].select('div.list')[0].select('tr.tda')
    tdbDetails = soup.select('div.p_details')[0].select('div.tab_container')[1].select('div.tab_content')[0].select('div.related_articles')[0].select('div.list')[0].select('tr.tdb')
    for eachTda in range(len(tdaDetails)):
       fitsToDict['JM-No.'] = descriptionDict['jm_no']
       makeModel = tdaDetails[eachTda].select('td')[0].select('a')[0].text
       fitsToDict['Make'] = ''.join(makeModel.split()[:1])
       fitsToDict['Model'] = ' '.join(makeModel.split()[1:])
       fitsToDict['Code'] = tdaDetails[eachTda].select('td')[21].select('a')[0].text.strip()
       fitsToDict['typ'] = tdaDetails[eachTda].select('td')[22].select('a')[0].text.strip()
       fitsToDict['from'] = tdaDetails[eachTda].select('td')[23].select('a')[0].text.strip()
       fitsToDict['to'] = tdaDetails[eachTda].select('td')[24].select('a')[0].text.strip()
       fitsToDict['Year'] = int(tdaDetails[eachTda].select('td')[25].select('a')[0].text.strip())
       fitsToDict['Cylinder'] = int(tdaDetails[eachTda].select('td')[26].select('a')[0].text.strip())
       fitsToDict['Performance'] = tdaDetails[eachTda].select('td')[27].select('a')[0].text.strip()
       fitsToDF = pd.concat([fitsToDF, pd.DataFrame(fitsToDict, index=[0])])
    for eachTdb in range(len(tdbDetails)):
       fitsToDict['JM-No.'] = descriptionDict['jm_no']
       makeModel = tdbDetails[eachTdb].select('td')[0].select('a')[0].text
       fitsToDict['Make'] = ''.join(makeModel.split()[:1])
       fitsToDict['Model'] = ' '.join(makeModel.split()[1:])
       fitsToDict['Code'] = tdbDetails[eachTdb].select('td')[21].select('a')[0].text.strip()
       fitsToDict['typ'] = tdbDetails[eachTdb].select('td')[22].select('a')[0].text.strip()
       fitsToDict['from'] = tdbDetails[eachTdb].select('td')[23].select('a')[0].text.strip()
       fitsToDict['to'] = tdbDetails[eachTdb].select('td')[24].select('a')[0].text.strip()
       fitsToDict['Year'] = int(tdbDetails[eachTdb].select('td')[25].select('a')[0].text.strip())
       fitsToDict['Cylinder'] = int(tdbDetails[eachTdb].select('td')[26].select('a')[0].text.strip())
       fitsToDict['Performance'] = tdbDetails[eachTdb].select('td')[27].select('a')[0].text.strip()
       fitsToDF = pd.concat([fitsToDF, pd.DataFrame(fitsToDict, index=[0])])
    # print(fitsToDF)
    descriptionDict['fitsToDataFrame'] = fitsToDF
    return descriptionDict


def scrapeData():
    fitsToList = []
    fitsToDF = pd.DataFrame()

    response = session.get(url)
    # soup = BeautifulSoup(data.content, 'html.parser')
    soup = BeautifulSoup(response.content, 'lxml')
    # print(soup)

    jm_no_list,title_list,brand_list,to_fit_make_list,sub_type_list,to_fit_model_list,intended_use_list,ean_list,quantity_list,condition_list,purchase_price_list,retail_price_list,image_list,image2_list,description_list,fitment_list = ([] for i in range(16))

    breadcrumpList = soup.select('div.breadcrump-liste')
    for eachbreadcrump in breadcrumpList:
        last_pde = eachbreadcrump.find('a', class_='last_pde').text
        middle_pde_list = eachbreadcrump.find_all('a', class_='middle_pde')
        middle_pde = middle_pde_list[1].text
        
    gallery_element = soup.select('div.gal_elem')
    # print(gallery_element)
    for id,eachElement in enumerate(gallery_element):
        gal_content = eachElement.find('div', class_='gal_content')
        gal_basket = eachElement.find('div', class_='gal_basket')
        # jm_no = gal_content.find('div', class_='gal_artnr').text
        # jm_no_list.append(jm_no[8:].replace(u'\xa0',''))
        title_list.append((eachElement.h3.a).text)
        brand = gal_content.find('div', class_='gal_text').text
        brand_list.append(brand.replace(u'\xa0','').strip())
        to_fit_make_list.append('')
        sub_type_list.append(last_pde)
        to_fit_model_list.append('')
        intended_use_list.append(middle_pde)
        ean_list.append('')
        condition_list.append('')
        # table = gal_basket.find('table')
        # purchase_price = table.find('tr', class_='tda').select('td')[0].find('table', class_='no_space').select('tr')[0].select('td.gal_price_color')[1].text
        # purchase_price_list.append(purchase_price[2:])
        # retail_price = table.find('tr', class_='tda').select('td')[0].find('table', class_='no_space').select('tr')[1].select('td.larsson_size')[0].text
        # retail_price_list.append(retail_price[2:])
        # gal_image = gal_content.find('div', class_='gal_image').select('a')[0].select('img')
        # image = gal_image[0]['src'].replace('//','https://')
        # image_list.append(image)
        # image2_list.append('')

        descriptionURL = str(eachElement.h3.a['href'])
        scrapeDescriptionData = scrapeDescription(descriptionURL, fitsToDF)
        fitsToDF = scrapeDescriptionData['fitsToDataFrame']
        quantity_list.append(scrapeDescriptionData['quantity'])
        jm_no_list.append(scrapeDescriptionData['jm_no'])
        purchase_price_list.append(scrapeDescriptionData['purchase_price'])
        retail_price_list.append(scrapeDescriptionData['retail_price'])
        image_list.append(scrapeDescriptionData['image'])
        image2_list.append('')
        description_list.append(scrapeDescriptionData['description'])
        # fitment_list.append(scrapeDescriptionData['fitment'])
        print("[%-30s] %d%%" % ('='*id, 3.3*(id+1)))
    
    scrapingData = {
        'JM-No.': jm_no_list, 'Title': title_list, 'Brand': brand_list, 'To Fit Make': to_fit_make_list, 'Sub Type': sub_type_list,
        'To Fit Model': to_fit_model_list, 'Intended Use': intended_use_list, 'EAN': ean_list, 'Quantity': quantity_list, 
        'Manufacturer Part Number': jm_no_list, 'Condition': condition_list, 'Purchase Price': purchase_price_list, 'Retail Price': retail_price_list, 
        'Image': image_list, 'Image 2': image2_list, 'Image 3': image2_list, 'Image 4': image2_list, 'Description': description_list
    }
    
    data = pd.DataFrame(scrapingData)
    # print(data)
    # data.to_csv('result.csv',index=False)
    writer = pd.ExcelWriter('result.xlsx')
    data.to_excel(writer, index=False)
    writer.save()
    writer = pd.ExcelWriter('fits_to.xlsx')
    fitsToDF.to_excel(writer, index=False)
    writer.save()
    print("Data Scraped Successfully")
    
if __name__=='__main__':
    scrapeData()