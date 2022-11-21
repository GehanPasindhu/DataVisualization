import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser
st.set_page_config(
    page_title="Web Scraper",
    page_icon="bar_chart",
    layout="wide"
)
st.markdown("<h1>Unsplash Web Scraper</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword=st.text_input("Enter your keyword")
    search = st.form_submit_button("Scrape")
placeholder = st.empty()
if keyword:
    page= requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content,'lxml')
    rows = soup.find_all("div", class_="ripi6")
    col1,col2,col3,col4,col5, col6 = placeholder.columns(6) 
    for index,row in enumerate(rows):
        figure = row.find_all("figure")
        for i in range(6):
            img = figure[i].find("img", class_="YVj9w")
            list = img["srcset"].split("?")
            anchor = figure[i].find("a", class_="rEAWd")
            print(i)
            if i==0:
                col1.image(list[0])
                btn=col1.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
            if i==1:
                col2.image(list[0])
                btn=col2.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
            if i==2:
                col3.image(list[0])
                btn=col3.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
            if i==3:
                col4.image(list[0])
                btn=col4.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
            if i==4:
                col5.image(list[0])
                btn=col5.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])  
            if i==5:
                col6.image(list[0])
                btn=col6.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])