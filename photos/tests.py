from django.test import TestCase
from .models import Category, Photo

# Create your tests here.

class CategoryTestClass(TestCase):

    def setUp(self):
        self.travel= Category(name = 'Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))

    def test_save_method(self):
        self.travel.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)      



class PhotoTestClass(TestCase): 
    def setUp(self):
        # Creating a new category and saving it
        self.travel= Category(name = 'Travel')
        self.travel.save_category()

        # Creating a new image and saving it

        self.new_image= Photo(image = 'travel.jpg', description= 'Travel around the world',date_created='2022-05-03')
        self.new_image.save()

        self.new_image.add(self.new_image)  


    def tearDown(self):
       Category.objects.all().delete()
       Photo.objects.all().delete()         