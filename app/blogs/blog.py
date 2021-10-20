from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='b20c0b06478844d5ad9576bce026d977')

# /v2/everything
all_articles = newsapi.get_everything(q='foods-diabetes',
                                      language='en',
                                      page=1)

#print(all_articles)

#print('\n'+str(type(all_articles)))

#https://lexper.p.rapidapi.com/v1.1/extract

print(type(all_articles['articles'][0]))

for article in all_articles['articles'][:min(all_articles['totalResults'], 10)]:
    title = article['title']
    url = article['url']
    img = article['urlToImage']

    print(title, '\n', url, '\n', img, '\n')