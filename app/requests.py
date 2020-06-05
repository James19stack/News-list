# from app import app
import urllib.request,json
from .models import Source
from .models import Article

# Source = source.Source
# Article = articles.Article
# headlines = 'top-headlines'


# Getting api key
api_key = None
base_url = None
top_base_url = None

def configure_request(app):
    global api_key,base_url,top_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    top_base_url = app.config['TOP_API_BASE_URL']

def get_source(sources):
    '''
    function that gets the json response to url request
    '''
    get_news_url = base_url.format(sources,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)


        new_results = None 

        if get_news_response['sources']: 
            new_results_list = get_news_response['sources']
            new_results = process_results(new_results_list)

    return new_results 

def process_results(news_list):
    news_results = []

    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')

        news_object = Source(id,title,description,url)
        news_results.append(news_object)

    return news_results

def get_articles():
    '''
    function that gets json response to our url request
    '''
    get_articles_url = top_base_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_article_data = url.read()
        get_articles_response = json.loads(get_article_data)


        news_articles = None

        if  get_articles_response['articles']:
            news_articles_list=  get_articles_response['articles']
            news_articles = process_articles(news_articles_list)

    return news_articles

def process_articles(article_list):
    '''
    process results of getting articles and create article objects
    '''
    news_articles = []

    for article_item in article_list:
        title = article_item.get('title')  
        description = article_item.get('description') 
        image = article_item.get('urlToImage')
        time = article_item.get('publishedAt')
        content = article_item.get('content')
        url = article_item.get('url')

        news_object = Article(title,description,image,time,content,url)
        news_articles.append(news_object)
           
    return news_articles  

def search_source(source_name):
        search_source_url = 'https://newsapi.org/v2/sources?country=us&apiKey={}&query={}'.format(api_key,source_name)
        with urllib.request.urlopen(search_source_url) as url:
            search_source_data = url.read()
            search_source_response =json.loads(search_source_data)

            search_news_results = None

            if search_source_response['sources']:
                search_news_list = search_source_response['sources']
                search_news_results = process_results(search_news_list)

        return search_news_results                    