class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,title,description,urlToImage,publishedAt,content,url):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.url = url


class Source:
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
