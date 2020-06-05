import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    
    def setUp(self):
        self.new_source = Source(1234,"newyork")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        self.assertEqual(self.new_source.id,1234)
        self.assertEqual(self.new_source.name,"newyork")
        

# if __name__ == '__main__':
#         unittest.main()           
