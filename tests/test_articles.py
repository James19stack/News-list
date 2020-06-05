import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setup(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("20 more people dead","It was a long car accident","null",10,"A lot of things",'http//bbc')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        self.assertEqual(self.new_article.title,"20 more people dead")
        self.assertEqual(self.new_article.description,"It was a long car accident") 
        self.assertEqual(self.new_article.urlToImage,"null")
        self.assertEqual(self.new_article.publishedAt,10)
        self.assertEqual(self.content,"Alot of things")
        self.assertEqual(self.new_article.url,"http//bbc")


# if __name__ == '__main__':
#         unittest.main()           


