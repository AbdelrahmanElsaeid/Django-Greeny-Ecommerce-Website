from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product, Brand

# Create your tests here.

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        new_brand = Brand.objects.create(
            name = 'New brand',
            image = SimpleUploadedFile(name='test_image.jpg', content=open("C:/Users/20128/Desktop/coding.jpeg", 'rb').read(),content_type='image/jpg')
        )

        Product.objects.create(
            name = 'product1',
            sku = 3232,
            brand=new_brand,
            price = 100,
            flag = 'New',
            description = 'test desc',
            subtitle = 'good product',
            image = SimpleUploadedFile(name='test_image.jpg', content=open("C:/Users/20128/Desktop/coding.jpeg", 'rb').read(),content_type='image/jpg')

        )

        # Test Models 
        def test_product_name_label(self):
            product = Product.objects.get(id=1)
            field_label = product._meta.get_field('name').verbose_name
            self.assertEquel(field_label, 'name')

        def test_firest_name_maxlength(self):
            product = Product.objects.get(id=1)
            field_label = product._meta.get_field('name').max_length
            self.assertEquel(field_label, 120)    


       # Test Views
        def test_view_url_exists_at_desired_location(self):
            response = self.client.get('/products/')
            self.assertEqual(response.status_code,200)    