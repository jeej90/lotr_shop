from sqlalchemy import update

from application import db
from application.models import Customer, Address, RegisteredUser, Product, Size, ProductCategory, Colour, Image

# product images

# img_1 = Image(name='arwen_evenstar_keyring.jpg')
# db.session.add(img_1)
# db.session.commit()

# connecting image to product

# image_product_1 = Product(image_id=1)

image_product_1 = (
    update(Product).
    where(Product.id == 2).
    values(image_id=1)
)
db.session.add(image_product_1)
db.session.commit()