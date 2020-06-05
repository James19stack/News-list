import os

class Config:
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?country=us&apiKey={}'    
    TOP_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
   
    pass

class DevConfig(Config):
    DEBUG = True 

config_options = {
'development':DevConfig,
'production':ProdConfig    
}      