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
response = session.get("https://mike.larsson.uk.com/en/category/10320000000/?sr=60")

soup = BeautifulSoup(response.content, 'lxml')
# print(soup)


def scrapeData():
    # soup = BeautifulSoup(data.content, 'html.parser')
    jm_no_list,title_list,brand_list,to_fit_make_list,sub_type_list,to_fit_model_list,intended_use_list,ean_list,quantity_list,condition_list,purchase_price_list,retail_price_list,image_list,image2_list,description_list,fitment_list = ([] for i in range(16))

    breadcrumpList = soup.select('div.breadcrump-liste')
    for eachbreadcrump in breadcrumpList:
        last_pde = eachbreadcrump.find('a', class_='last_pde').text
        middle_pde_list = eachbreadcrump.find_all('a', class_='middle_pde')
        middle_pde = middle_pde_list[1].text
        
    gallery_element = soup.select('div.gal_elem')
    # print(gallery_element)
    for eachElement in gallery_element:
        gal_content = eachElement.find('div', class_='gal_content')
        gal_basket = eachElement.find('div', class_='gal_basket')
        jm_no = gal_content.find('div', class_='gal_artnr').text
        jm_no_list.append(jm_no[8:].replace(u'\xa0',''))
        title_list.append((eachElement.h3.a).text)
        brand = gal_content.find('div', class_='gal_text').text
        brand_list.append(brand.replace(u'\xa0','').strip())
        to_fit_make_list.append('')
        sub_type_list.append(last_pde)
        to_fit_model_list.append('')
        intended_use_list.append(middle_pde)
        ean_list.append('')
        quantity_list.append(1)
        condition_list.append('New')
        table = gal_basket.find('table')
        purchase_price = table.find('tr', class_='tda').select('td')[0].find('table', class_='no_space').select('tr')[0].select('td.gal_price_color')[1].text
        purchase_price_list.append(purchase_price[2:])
        retail_price = table.find('tr', class_='tda').select('td')[0].find('table', class_='no_space').select('tr')[1].select('td.larsson_size')[0].text
        retail_price_list.append(retail_price[2:])
        gal_image = gal_content.find('div', class_='gal_image').select('a')[0].select('img')
        image = gal_image[0]['src'].replace('//','https://')
        image_list.append(image)
        image2_list.append('')
        description_list.append('')
        fitment_list.append('')

    scrapingData = {
        'JM-No.': jm_no_list, 'Title': title_list, 'Brand': brand_list, 'To Fit Make': to_fit_make_list, 'Sub Type': sub_type_list,
        'To Fit Model': to_fit_model_list, 'Intended Use': intended_use_list, 'EAN': ean_list, 'Quantity': quantity_list, 
        'Manufacturer Part Number': jm_no_list, 'Condition': condition_list, 'Purchase Price': purchase_price_list, 'Retail Price': retail_price_list, 
        'Image': image_list, 'Image 2': image2_list, 'Image 3': image2_list, 'Image 4': image2_list, 'Description': description_list, 'Fitment': fitment_list
    }

    data = pd.DataFrame(scrapingData)
    print(data)
    print("Data Scraped Successfully")
    # data.to_excel("result.xlsx")
    data.to_csv('result.csv',index=False)

if __name__=='__main__':
    scrapeData()