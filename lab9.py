#task1
import requests
from bs4 import BeautifulSoup

def loadPage(url):
    response = requests.get(url, headers = {"User-Agent": "YaBrowser/26.3.5.782"})
    response.raise_for_status()
    return response.text

def parseNews(html):
    soup = BeautifulSoup(html, "html.parser")
    newsItems = []

    for item in soup.select(".tl_item"):
        linkTag = item.find("a", href=True)
        if not linkTag:
            continue

        timeTag = item.select_one(".tl_date span")
        titleTag = item.select_one(".tl_news")
        categoryTag = item.select_one(".tl_node")

        newsItems.append({
            "time": timeTag.get_text(strip=True) if timeTag else "",
            "title": titleTag.get_text(strip=True) if titleTag else "",
            "category": categoryTag.get_text(strip=True) if categoryTag else "",
            "url": linkTag["href"],
        })

    return newsItems

def displayNews(news_list):
    print(f"БелТА — Все новости")

    for i, news in enumerate(news_list, 1):
        print(f"[{i}] {news['time']}  [{news['category']}]  {news['title']}")
        print(f"{news['url']}")
        print()

    print(f"Всего новостей: {len(news_list)}")

html = loadPage('https://belta.by/all_NeWS/')
news = parseNews(html)
displayNews(news)

#task2
def fetchWeather(**kwargs):
    response = requests.get(BASE_URL, params=kwargs)
    response.raise_for_status()
    return response.json()

def displayWeather(data):
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    print(f"Погода: {city}, {country}")
    print(f"Описание: {description.capitalize()}")
    print(f"Температура: {temp}°C (ощущается как {feels_like}°C)")
    print(f"Влажность: {humidity}%")
    print(f"Ветер: {wind_speed} м/с")

city = input("Введите город: ")
API_KEY = "8d3cbe11aa4089c07f41f2e3c03de47d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

data = fetchWeather(q = city, appid = API_KEY, units = "metric", lang =  "ru")
displayWeather(data)