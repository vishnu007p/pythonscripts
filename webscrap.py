from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    values=soup.find_all("span", class_="amt")
    data=[]
    for v in values:
        item={}
        item["tablename"]=v.find("tag",class_="classname")
        item["tablename"]=v.find("tag",class_="classname")
        data.append(item)
    return data
def dataexport(data):
    df= pd.DataFrame(data)
    df.to_excel("values.xlsx")
    df.to_csv("values.csv")

if __name__ == '__main__':
    data=get_data("https://www.moneycontrol.com/mutual-funds/nav/axis-bluechip-fund-regular-plan/MAA009")
    dataexport(data)
    print("success")