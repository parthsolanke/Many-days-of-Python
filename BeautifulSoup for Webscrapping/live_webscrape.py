import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
# grabbing the article titles and links
articles = soup.find_all(name="a", attrs={"rel": "noreferrer"})
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

# grabbing the article scores
article_upvotes = [int(scores.getText().split()[0])
                   for scores in soup.find_all(name="span", class_="score")]

largest_num_idx = article_upvotes.index(max(article_upvotes))
print(max(article_upvotes))
print(largest_num_idx)
print(article_texts[largest_num_idx])

