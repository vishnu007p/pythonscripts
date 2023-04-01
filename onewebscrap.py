from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    item={}
    value=soup.find("span", class_="amt")

    # data=[]
    # data.append(values)
# def dataexport(v):
    df= pd.DataFrame(value)
    df.to_excel("data.xlsx")
    df.to_csv("data.csv")

if __name__ == '__main__':
    data=get_data("https://www.moneycontrol.com/mutual-funds/nav/axis-bluechip-fund-regular-plan/MAA009")
    # dataexport(data)
    print("success")