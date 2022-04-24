from application import db
from application.models import Customer, Address, RegisteredUser, Product, Size, ProductCategory, Colour

# db.drop_all()
# db.create_all()

# foreign keys input first

# size
# size_xs = Size(size="XS")
# size_s = Size(size="S")
# size_m = Size(size="M")
# size_l = Size(size="L")
# size_xl = Size(size="XL")
#
# sizes = [size_xs, size_s, size_m, size_l, size_xl]
# # sizes = [size_s, size_m, size_l, size_xl]
#
# db.session.add_all(sizes)
# # db.session.add(size_xs)
#
# db.session.commit()
#
# # product_category
#
# product_category_1 = ProductCategory(category="Clothes")
# product_category_2 = ProductCategory(category="Games")
# product_category_3 = ProductCategory(category="Keyrings & Badges")
# product_category_4 = ProductCategory(category="Collectibles")
#
# product_categories = [product_category_1, product_category_2, product_category_3, product_category_4]
#
# db.session.add_all(product_categories)
# db.session.commit()
#
# # colour
#
# colour_1 = Colour(colour='White')
# colour_2 = Colour(colour='Black')
# colour_3 = Colour(colour='Red')
# colour_4 = Colour(colour='Blue')
# colour_5 = Colour(colour='Green')
# colour_6 = Colour(colour='Yellow')
# colour_7 = Colour(colour='Orange')
# colour_8 = Colour(colour='Grey')
# colour_9 = Colour(colour='Brown')
# colour_10 = Colour(colour='Purple')
# colour_11 = Colour(colour='Beige')
# colour_12 = Colour(colour='Pink')
#
# colours = [colour_1, colour_2, colour_3, colour_4, colour_5, colour_6, colour_7, colour_8, colour_9, colour_10, colour_11, colour_12]
#
# db.session.add_all(colours)
#
# db.session.commit()
#
# # products!

# product1 = Product(name='Aragorn V-neck T-shirt', description="The Lord of the Rings Aragorn V-Neck T-Shirt, Black, 100% cotton White t-shirt of 100% cotton", full_price="25.00", barcode="1028974591628", size_id=4, colour_id=2, product_category_id=1)
#
# db.session.add(product1)
# db.session.commit()

# need to resolve stock management control issue based on tables for different sizes of same product
# db.session.add(testUser1)


# adam = "Adam"
# result = RegisteredUser.query.filter_by(user_name=adam).first()
# print(result)


