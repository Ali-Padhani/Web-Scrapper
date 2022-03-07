from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import time

import re 
  
def remove(string): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '-', string) 

def to_lower_case(s):
    return str(s).lower()

def get_table_headers(table):
    """Given a table soup, returns all the headers"""
    headers = []
    for th in table.find("tr", attrs={'class':'tableHead'}).find_all("td"):
        headers.append(th.text.strip())
    return headers

def get_table_rows(table):
    """Given a table, returns all its rows"""
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        # grab all td tags in this table row
        tds = tr.find_all("td")
        if len(tds) == 0:
            # if no td tags, search for th tags
            # can be found especially in wikipedia tables below the table
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            # use regular td tags
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)
    return rows

def save_as_csv(table_name, headers, rows):

    import os
    df = pd.DataFrame(rows, columns=headers)
    # if file does not exist write header 
    if not os.path.isfile(f"{table_name}.csv"):
        print("Saving")
        df.to_csv(f"{table_name}.csv")
        #pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv")
    else: # else it exists so append without writing the header
        print(" Else Saving")
        df.to_csv(f"{table_name}.csv", mode='a', header=False)
        #pd.DataFrame(rows, columns=None).to_csv(f"{table_name}.csv", mode = 'a')


def get_all_tables(scrapper, brand):
    
    for sr in scrapper:
    
        try:
            be = to_lower_case(brand)
            be = be.replace('tires', '')
            br = remove(be)
            print (Baseurl+'/'+br+sr+tire)
            #driver.get(Baseurl+accelera+"-"+sr+tire)
            driver.get(Baseurl+'/'+br+sr+tire)

            content = driver.page_source
            soup = BeautifulSoup(content,features="html.parser")

            #for a in soup.findAll('table', attrs={'class':'specification table'}):
            tables = soup.findAll('table', attrs={'class':'specification table'})
            try:

                img = soup.find('img', attrs={'class': 'tireprev center-block'})
                img_link = img.get('src')
            except:
                div = soup.find('div', attrs={'class': 'item active'})
                img = div.find('img', attrs={'class': 'tireprev center-block resize_fit_center catalog-product-image'})
                img_link = img.get('src')
                
            print (img)
            print (img_link)
            urllib.request.urlretrieve(brand/img_link, brand+" "+sr+".jpg")
            time.sleep(3)
                
            
            print(f"[+] Found a total of {len(tables)} tables.")
            # iterate over all tables
            for i, table in enumerate(tables, start=1):
                # get the table headers
                headers = get_table_headers(table)
                headers.insert(0,"Brand")
                print ("Headers", headers)
                # get all the rows of the table
                rows = get_table_rows(table)

                for row in rows:
                    row.insert(0,brand+" "+sr)
                
                print("Rows: ", rows)
                
                # save table as csv file
                        
                table_name = f"table-{i}"
                print(f"[+] Saving {table_name}")
                save_as_csv(table_name, headers, rows)
            
            

        except :
            pass

    
        




    


driver = webdriver.Chrome("C:\Program Files\Java\chromedriver")

Baseurl =  "https://simpletire.com"
path = "/tire-brands"

driver.get(Baseurl+path)
#driver.get(Baseurl+accelera+tire)

content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
accelera = "achilles"
tire = "-tires/"

brandname = []
brandURL = []

for div in soup.find_all('div', attrs={'class':'col-md-3 col-sm-4'}):
    
    for a in div.find_all('a', href=True):
        #print('{} - {}'.format(a.get_text(strip=True), a['href']))
        brandname.append(a.get_text(strip=True))
        brandURL.append(a['href'])
print ("Brand Name: ", brandname)
print ("Brand URL: ", brandURL)




""" 
for brand, Brandurl in zip(brandname, brandURL):
    driver.get(Baseurl+Brandurl)
    content = driver.page_source
    soup = BeautifulSoup(content,features="html.parser")

    names = []
    
    for a in soup.findAll('a',href=True, attrs={'class':'productLine'}):
        names.append(a.text)
        
    print ("NAmes: ",names)

    name_lower = list(map(to_lower_case,names))



    pro= []

    for name in name_lower:
    
        nm = name.replace("/","-")
        nm = remove(nm)
    
        #print(nm)
        pro.append(nm)

    print("pro: ", pro)

#driver.close()

#tags = get_data(pro)



#dfs = pd.read_html(str(tags))[0]
#dfs.to_csv('data.csv')

    get_all_tables(pro, brand)
driver.close()


     """








# print(f"[+] Found a total of {len(tables)} tables.")
#     # iterate over all tables
# for i, table in enumerate(tables, start=1):
#     # get the table headers
#     headers = get_table_headers(table)
#     headers.insert(0,"Brand")
#     print ("Headers", headers)
#     # get all the rows of the table
#     rows = get_table_rows(table)
#     print (len(rows))
    
#     for j, row in enumerate(rows, start=0):
#         row.insert(0,accelera+" "+pro[i])
    
#     print("Rows: ", rows)
    
#     # save table as csv file
            
#     table_name = f"table-{i}"
#     print(f"[+] Saving {table_name}")
#     save_as_csv(table_name, headers, rows)

    




