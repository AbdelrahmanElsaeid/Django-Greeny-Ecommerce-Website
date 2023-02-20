import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from faker import Faker
import random
from product.models import Product, Brand,ProductImages



def seed_brand(n):
    fake = Faker()
    images = ['apple.jpg', 'Nokia.png', 'Huawei.png', 'Realme.png', 'oppo.png', 'Redmi.png', 'Samsung.png' ]
    for x in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f"brand/{images[random.randint(0,6)]}"

        )
    print(f"{n} Brand Seed ")





def seed_product(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg']
    flags = ['New', 'Feature', 'Sale']
    for x in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f"products/{images[random.randint(0,14)]}" ,
            price  = round(random.uniform(20.99, 99.99),2),
            sku = random.randint(1000,1000000),
            subtitle = fake.text(max_nb_chars = 300),
            description = fake.text(max_nb_chars = 4000),
            flag = flags[random.randint(0,2)],
            brand = Brand.objects.get(id = random.randint(1,120)),

        )

    print(f"{n} Product Seed ")


def seed_product_images(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg']
    for x in range(n):
        ProductImages.objects.create(
            Product = Product.objects.get(id = random.randint(1,5000)),
            image = f"productimages/{images[random.randint(0,14)]}" ,

        )
    print(f"{n} Product Image Seed ")


#seed_brand(100)
#seed_product(5000)
seed_product_images(10000)