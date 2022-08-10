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



def exportDF(scrapingData,fitsToDF,TechnicalDataDF):
    
    data = pd.DataFrame(scrapingData)
    # data.to_csv('result.csv',index=False)
    writer = pd.ExcelWriter('result.xlsx')
    data.to_excel(writer, index=False)
    writer.save()
    writer = pd.ExcelWriter('fits_to.xlsx')
    fitsToDF.to_excel(writer, index=False)
    writer.save()
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

def scrapeFitToList(descriptionURL, fitsToDF, ovid, jm_no):
    fitsToDict = {}
    # try:
    fit_to_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive','Referer': f'{descriptionURL}','Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin',
    }

    fit_to_params = {
        'request': 'getFList','shopname': '','ovid': f'{ovid}','sa_id': '','lang': 'en','vsr': 'all','ffilter': '',
    }

    fit_to_response = session.get('https://mike.larsson.uk.com/ajax.php', params=fit_to_params, headers=fit_to_headers)

    fit_to_soup = BeautifulSoup(fit_to_response.content, 'lxml')
    tdaDetails = fit_to_soup.select('div.related_articles')[0].select('div.list')[0].select('tr.tda')
    tdbDetails = fit_to_soup.select('div.related_articles')[0].select('div.list')[0].select('tr.tdb')
    for eachTda in range(len(tdaDetails)):
        fitsToDict['JM-No.'] = jm_no
        makeModel = tdaDetails[eachTda].select('td')[0].select('a')[0].text
        fitsToDict['Make'] = ''.join(makeModel.split()[:1])
        fitsToDict['Model'] = ' '.join(makeModel.split()[1:])
        fitsToDict['Code'] = tdaDetails[eachTda].select('td')[21].select('a')[0].text.strip()
        fitsToDict['typ'] = tdaDetails[eachTda].select('td')[22].select('a')[0].text.strip()
        fitsToDict['from'] = tdaDetails[eachTda].select('td')[23].select('a')[0].text.strip()
        fitsToDict['to'] = tdaDetails[eachTda].select('td')[24].select('a')[0].text.strip()
        fitsToDict['Year'] = tdaDetails[eachTda].select('td')[25].select('a')[0].text.strip()
        fitsToDict['Cylinder'] = tdaDetails[eachTda].select('td')[26].select('a')[0].text.strip()
        fitsToDict['Performance'] = tdaDetails[eachTda].select('td')[27].select('a')[0].text.strip()
        fitsToDF = pd.concat([fitsToDF, pd.DataFrame(fitsToDict, index=[0])])
    for eachTdb in range(len(tdbDetails)):
        fitsToDict['JM-No.'] = jm_no
        makeModel = tdbDetails[eachTdb].select('td')[0].select('a')[0].text
        fitsToDict['Make'] = ''.join(makeModel.split()[:1])
        fitsToDict['Model'] = ' '.join(makeModel.split()[1:])
        fitsToDict['Code'] = tdbDetails[eachTdb].select('td')[21].select('a')[0].text.strip()
        fitsToDict['typ'] = tdbDetails[eachTdb].select('td')[22].select('a')[0].text.strip()
        fitsToDict['from'] = tdbDetails[eachTdb].select('td')[23].select('a')[0].text.strip()
        fitsToDict['to'] = tdbDetails[eachTdb].select('td')[24].select('a')[0].text.strip()
        fitsToDict['Year'] = tdbDetails[eachTdb].select('td')[25].select('a')[0].text.strip()
        fitsToDict['Cylinder'] = tdbDetails[eachTdb].select('td')[26].select('a')[0].text.strip()
        fitsToDict['Performance'] = tdbDetails[eachTdb].select('td')[27].select('a')[0].text.strip()
        fitsToDF = pd.concat([fitsToDF, pd.DataFrame(fitsToDict, index=[0])])
    return fitsToDF
    # except Exception as e:
    #     print(f"Error : ",e)
def scrapeDescription(descriptionURL, fitsToDF, technicalDataDF, ovid):
    descriptionDict = {}
    # try:
    descriptionResponse = session.get(descriptionURL)
    soup = BeautifulSoup(descriptionResponse.content, 'lxml')
    mm_detail_container = soup.select('div.p_details')[0].select('div.mm_detail_container')
    mm_details = mm_detail_container[0].select('div.mm_details')
    if soup.find_all("div", {"class": "mm_mini"}):
        imageCount = len(mm_detail_container[0].select('div.mm_mini')[0].select('a'))
        if imageCount > 3: image4 = mm_detail_container[0].select('div.mm_mini')[0].select('a')[3]['href'].replace('//','https://').replace(' ','')
        else: image4 = ''
        if imageCount > 2: image3 = mm_detail_container[0].select('div.mm_mini')[0].select('a')[2]['href'].replace('//','https://').replace(' ','')
        else: image3 = ''
        if imageCount > 1: image2 = mm_detail_container[0].select('div.mm_mini')[0].select('a')[1]['href'].replace('//','https://').replace(' ','')
        else: image2 = ''
        image1 = mm_detail_container[0].select('div.mm_mini')[0].select('a')[0]['href'].replace('//','https://').replace(' ','')
    else:
        if mm_detail_container[0].select('div.mm_images')[0].select('div.mm_images_box')[0].select('a') != []: image1 = mm_detail_container[0].select('div.mm_images')[0].select('div.mm_images_box')[0].select('a')[0]['href'].replace('//','https://')
        else: image1 = ''
        image2 = image3 = image4 = ''

    descriptionDict['image'] = image1
    descriptionDict['image2'] = image2
    descriptionDict['image3'] = image3
    descriptionDict['image4'] = image4

    descriptionDict['jm_no'] = mm_details[0].select('div.mm_drow')[0].find('div',class_='mm_right').text

    desc_count = len(mm_details[0].select('div.mm_drow'))
    descNameList = []
    for eachDesc in range(desc_count):
        descNameList.append(mm_details[0].select('div.mm_drow')[eachDesc].select('div.mm_left')[0].text)
    if 'Manufacturer no.:' in descNameList:
        descIndex = descNameList.index('Manufacturer no.:')
        descriptionDict['manufacturer_part_number'] = mm_details[0].select('div.mm_drow')[descIndex].select('div.mm_right')[0].text
    else: descriptionDict['manufacturer_part_number'] = ''
    if 'Minimum order quantity:' in descNameList:
        descIndex = descNameList.index('Minimum order quantity:')
        descriptionDict['quantity'] = mm_details[0].select('div.mm_drow')[descIndex].select('div.mm_right')[0].text
    else: descriptionDict['quantity'] = ''
    if soup.select('div.p_details')[0].select('div.tab_container') == []: 
        descriptionDict['description'] = ''
    else:
        if soup.select('div.p_details')[0].select('div.tab_container')[0].h4.text == 'Description':
            description_list = soup.select('div.p_details')[0].select('div.tab_container')[0].select('div.goog_trans_cont')[0].select('div.goog_trans_res')[0].select('p')
            descriptionDict['description'] = ' '.join([each_description.text.replace(u'\xa0','') for each_description in description_list])
        else:
            print("Description Blank")
            descriptionDict['description'] = ''
    
        tab_count = len(soup.select('div.p_details')[0].select('div.tab_container'))
        tabNameList = []
        for eachTab in range(tab_count):
            tabNameList.append(soup.select('div.p_details')[0].select('div.tab_container')[eachTab].h4.text)
        if 'Fits to:' in tabNameList:
            fitsToDF = scrapeFitToList(descriptionURL, fitsToDF, ovid, descriptionDict['jm_no'])
        if 'Technical data' in tabNameList:
            tabIndex = tabNameList.index('Technical data')
            technicalDataDF = scrapeTechnicalDataList(soup, tabIndex, technicalDataDF, descriptionDict['jm_no'])
        
    descriptionDict['fitsToDataFrame'] = fitsToDF
    descriptionDict['technicalDataDataFrame'] = technicalDataDF
    return descriptionDict
    # except Exception as e:
    #     print(f"Error : ",e)

def scrapeData(url, category_count):
    
    jm_no_list,title_list,brand_list,to_fit_make_list,sub_type_list,to_fit_model_list,intended_use_list,ean_list,quantity_list,manufacturer_part_number_list,condition_list,purchase_price_list,retail_price_list,image_list,image2_list,image3_list,image4_list,description_list = ([] for i in range(18))
    
    # try:
    fitsToDF = pd.DataFrame()
    technicalDataDF = pd.DataFrame()
    for num in range(3690,category_count,30):
        if num == 0: page = 1
        else: page = (num/30)+1
        response = session.get(f"{url}/?sr={num}")
        soup = BeautifulSoup(response.content, 'lxml')
        breadcrumpList = soup.select('div.breadcrump-liste')
        for eachbreadcrump in breadcrumpList:
            last_pde = eachbreadcrump.find('a', class_='last_pde').text
            middle_pde_list = eachbreadcrump.find_all('a', class_='middle_pde')
            middle_pde = middle_pde_list[1].text
            
        gallery_element = soup.select('div.gal_elem')
        print(f"Page : {int(page)}")
        
        for id,eachElement in enumerate(gallery_element):
            gal_content = eachElement.find('div', class_='gal_content')
            gal_basket = eachElement.find('div', class_='gal_basket')
            title_list.append((eachElement.h3.a).text)
            brand = gal_content.find('div', class_='gal_text').text
            brand_list.append(brand.replace(u'\xa0','').strip())
            to_fit_make_list.append('')
            sub_type_list.append(last_pde)
            to_fit_model_list.append('')
            intended_use_list.append(middle_pde)
            ean_list.append('')
            condition_list.append('')
            table = gal_basket.find('table')
            if table.select('tr')[1].select('td')[0].text == 'Trade':
                purchase_price = table.select('tr')[3].select('td')[1].text
                retail_price = table.select('tr')[4].select('td')[1].text
            else:
                purchase_price = table.select('tr')[1].select('td')[1].text
                retail_price = table.select('tr')[2].select('td')[1].text
            purchase_price_list.append(purchase_price[2:])
            retail_price_list.append(retail_price[2:])


            descriptionURL = str(eachElement.h3.a['href'])
            ovid = descriptionURL.replace('https://mike.larsson.uk.com/en/category/','').split('/')[-2]
            scrapeDescriptionData = scrapeDescription(descriptionURL, fitsToDF, technicalDataDF, ovid)
            fitsToDF = scrapeDescriptionData['fitsToDataFrame']
            technicalDataDF = scrapeDescriptionData['technicalDataDataFrame']
            quantity_list.append(scrapeDescriptionData['quantity'])
            jm_no_list.append(scrapeDescriptionData['jm_no'])
            manufacturer_part_number_list.append(scrapeDescriptionData['manufacturer_part_number'])
            image_list.append(scrapeDescriptionData['image'])
            image2_list.append(scrapeDescriptionData['image2'])
            image3_list.append(scrapeDescriptionData['image3'])
            image4_list.append(scrapeDescriptionData['image4'])
            description_list.append(scrapeDescriptionData['description'])
            print("[%-30s] %d%%" % ('='*id, 3.3*(id+1)))
        scrapingData = {
            'JM-No.': jm_no_list, 'Title': title_list, 'Brand': brand_list, 'To Fit Make': to_fit_make_list, 'Sub Type': sub_type_list,
            'To Fit Model': to_fit_model_list, 'Intended Use': intended_use_list, 'EAN': ean_list, 'Quantity': quantity_list, 
            'Manufacturer Part Number': manufacturer_part_number_list, 'Condition': condition_list, 'Purchase Price': purchase_price_list, 'Retail Price': retail_price_list, 
            'Image': image_list, 'Image 2': image2_list, 'Image 3': image3_list, 'Image 4': image4_list, 'Description': description_list
        }
        exportDF(scrapingData, fitsToDF, technicalDataDF)
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