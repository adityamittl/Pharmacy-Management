import requests
import bs4 as beautifulSoup
import json


def fetchDetail(name):
    composition = "Not Available"
    try:
        exactName = requests.get("https://www.apollopharmacy.in/search-medicines/{}".format(name))
        for c in exactName.cookies:
            print(c)
        soup = beautifulSoup.BeautifulSoup(exactName.text, 'html.parser')
        exactMedicine = soup.find_all('a', class_='ProductCard_proDesMain__gigTv')[0]
        link,name = exactMedicine.get('href'),exactMedicine.find('p',class_="ProductCard_productName__2LhTY").text
        # print(link)
        try:
            x = requests.get("https://www.apollopharmacy.in"+link)
            soup = beautifulSoup.BeautifulSoup(x.text, "html.parser")
            medicines = soup.find_all('script', class_='structured-data-list')
            for i in medicines:
                comp = i.contents
                for j in comp:
                    j = json.loads(str(j))
                    temp = j.get("activeIngredient")
                    if temp!= None:
                        composition = temp
        except:
            composition = "Not Available"
    except:
        name = "Not Available"
        composition = "Not Available"
    # print(composition)
    return name,composition
