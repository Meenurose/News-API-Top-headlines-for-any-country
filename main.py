import os
import requests

API_KEY = os.getenv("apikey")


def get_news(country):
  url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}"

  response = requests.get(url)
  content = response.json()
  articles = content['articles']
  news = []
  for article in articles:
    news.append(
      f"TITLE\n {article['title']}, \nDESCRIPTION\n{article['description']}")

  return news


print(get_news(country='in'))     # can use 2-letter ISO 3166-1 code of the country you want to get headlines for
