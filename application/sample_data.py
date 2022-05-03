
from application import db
from flask_login import current_user
from application.models import Customer, Address, RegisteredUser, Product, Size, Image, ProductCategory, Colour, Admin, Staff
from flask import session


# PRODUCT LIST

# all products from all categorys
# product1 = Product(name='Aragorn V-neck T-shirt', description="The Lord of the Rings Aragorn V-Neck T-Shirt, Black, 100% cotton White t-shirt of 100% cotton", full_price="25.00", barcode="1028974591628", colour_id=2, product_category_id=1)
# product2 = Product(name="Arwen Evenstar Keyring", description="3D replica of Arwen's pendant in white metal. 1.1x2.9\"/3x7 cm. In a giftbox.", full_price="10.00", barcode="786325544128", product_category_id=3)
# product3 = Product(name="Gandalf the Grey T-Shirt", description="Gandalf The Grey Premium Slim Fit T-Shirt.", full_price="24.00", barcode="5897524165555", colour_id=8, product_category_id=1)
# product4 = Product(name="The One Ring Enamel Pin Badge", description="Pin badge amde from high quality metal - Packaging with blister card. - Dimensions: 1.2x1.1\"/ H. 3cm x L. 2.6cm", full_price="5.50", barcode="9842563247151", product_category_id=3)
# product5 = Product(name="The One Ring Keyring", description="High quality silver coloured metal keychain is a subtly elgant memento inspired by The Lord of the Rings film trilogy - perfect for carrying a little piece of Middle Earth around in your pocket!", full_price="12.00", barcode="1785496587452", product_category_id=3)
# product6 = Product(name="Abystyle Lord Of The Rings - Lorien Leaf 3D Pin Badge", description="3D replica of Arwen's pendant in white metal. 1.1x2.9\"/3x7 cm. In a giftbox.", full_price="10.00", barcode="8521456987112", product_category_id=3)
# product7 = Product(name="Frodo Keyring", description="3Frodo POP! Keyring Character. Made from vinyl. Dimensions 2.54 x 2.54  x 3.81 cm.", full_price="8.00", barcode="3248561258741", product_category_id=3)
# product8 = Product(name="The Lord of the Rings Monopoly: Trilogy Edition", description="Chess set made complte with chess pieces, board and storage bags. Board dimensions 47x47x1cm", full_price="75.00", barcode="2547812547842", product_category_id=2)
# product9 = Product(name="Battle for Middle-earth Chess Set", description="Chess set made from plastic and card. Compete with chess pieces, board and storage bags. Board dimensions 47 x 47 x 1 centimetres", full_price="24.99", barcode="3254158749632", product_category_id=2)
# product10 = Product(name="Lord of the Rings Collectible Chess Set - Officially Licensed Film Set Movie Gifts", description="32 precise miniature sculptures crafted in fine pewter of actual cast members. Ancient map of Middle-earth mounted below the playing surface. The base features images of memorable characters and scenes from the trilogy. 15x15\" (38x38cm)", full_price="350.00", barcode="1479652365412", product_category_id=2)
# product11 = Product(name="The Lord of the Rings Playing Cards Standard Deck with Embossed Tin", description="Standard deck of playing cards with a section of the Middle Earth map as a background. Includes an embossed storage tin", full_price="12.00", barcode="5471124552136", product_category_id=2)
# product12 = Product(name="The Magic Hexagon Brain Teaser", description="Form a magic hexagon by joining the moviecards the right way. The box has as a bonus cut-out figures and part of a movie calendar", full_price="15.00", barcode="1224563125133", product_category_id=2)
# product13 = Product(name="Lord of the Rings Heroes of Middle Earth 1000 Piece Jigsaw Puzzle", description="Delve into the world of Lord of the Rings with this beautiful jigsaw puzzle where Aragorn, Éowyn, Gandalf, Sam, Frodo, Legolas and Gimli prepare for battle. 1000 pieces. 35.1 x 27.2 x 5.5 cm", full_price="15.99", barcode="2475113345262", product_category_id=2)
# product14 = Product(name="Gollum delux art figurine", description="Polystone gollum statue. 12 cm tall and comes with matching base.", full_price="19.99", barcode="2470013345269", product_category_id=2)
# product15 = Product(name="Lord of the Rings Gimli Figure", description="This Gimli is a 7-inch scale figure featuring 16 points of articulation, detailed sculpting and a full range of accessories. Comes packaged in a full-color window box with hangtag. 6.4 x 5.1 x 15.2cm", full_price="40.00", barcode="5482365121224", available_stock=6, product_category_id=4)
# product16 = Product(name="Lord of the Rings Legolas Action Figure", description="This Legolas is a 7-inch scale figure featuring 16 points of articulation, detailed sculpting and a full range of accessories. Comes packaged in a full-color window box with hangtag.  5.4 x 2.5 x 18.8cm", full_price="40.00", barcode="5911233215521", available_stock=5, product_category_id=4)
# product17 = Product(name="Lord of the Rings Galadriel Figurine", description="This Galadriel figurine is made of lead and painted by hand. Comes boxed with a magazine (in English) about the character in the saga. 30 x 20 x 10cm", full_price="40.00", barcode="1248555112322", available_stock=8, product_category_id=4)
# product18 = Product(name="Lord of the Rings Statue Gollum", description="Tortured and wrought wretched by the lure of the One Ring, Gollum is a withered, piteous creature. The most iconic creature from The Lord Of The Rings movie trilogy, Gollum was also a technological breakthrough. The statue is an Open Edition piece. 14 x 11 x 15cm", full_price="75.00", barcode="3225122445623", available_stock=5, product_category_id=4)
# product19 = Product(name="Elven Green Leaf Brooch Pin Pendant Necklace with Jewellery Box", description="Made from platinum and enamel. Necklace with a metal detailed jewellery box.Pendant Size :6.5*4.5CM Chain Length:50±2CM", full_price="75.00", barcode="2336125446325", available_stock=9, product_category_id=4)
# product20 = Product(name="Lord of the Rings Replica of The One Ring Necklace", description="Ring made for 24 carat gold, with inscription with all round. Box contents: in an jewellery box. Chain 60 cm; Ring Diameter: Approx. 20 mm, scale approx. 62 mm, Width approx. 7 mm", full_price="95.00", barcode="2263255124121", available_stock=12, product_category_id=4)
#
# products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12, product13, product14, product15, product16, product17, product18, product19, product20]
#
# db.session.add_all(products)
# db.session.commit()

#clothes category
# product1 = Product(name='Aragorn V-neck T-shirt', description="The Lord of the Rings Aragorn V-Neck T-Shirt, Black, 100% cotton White t-shirt of 100% cotton", full_price="25.00", barcode="1028974591628", size_id=4, colour_id=2, product_category_id=1)
#
# db.session.add(product1)
# db.session.commit()

# keyring and badges category
# product2 = Product(name="Arwen Evenstar Keyring", description="3D replica of Arwen's pendant in white metal. 1.1x2.9\"/3x7 cm. In a giftbox.", full_price="10.00", barcode="786325544128", product_category_id=3)
#
# db.session.add(product2)
# db.session.commit()


# clothes category
# product3 = Product(name="Gandalf the Grey T-Shirt", description="Gandalf The Grey Premium Slim Fit T-Shirt.", full_price="24.00", barcode="5897524165555", size_id=3, colour_id=8, product_category_id=1)
#
# db.session.add(product3)
# db.session.commit()


# keyring and badges category
# product4 = Product(name="The One Ring Enamel Pin Badge", description="Pin badge amde from high quality metal - Packaging with blister card. - Dimensions: 1.2x1.1\"/ H. 3cm x L. 2.6cm", full_price="5.50", barcode="9842563247151", product_category_id=3)
# product5 = Product(name="The One Ring Keyring", description="High quality silver coloured metal keychain is a subtly elgant memento inspired by The Lord of the Rings film trilogy - perfect for carrying a little piece of Middle Earth around in your pocket!", full_price="12.00", barcode="1785496587452", product_category_id=3)
# product6 = Product(name="Abystyle Lord Of The Rings - Lorien Leaf 3D Pin Badge", description="3D replica of Arwen's pendant in white metal. 1.1x2.9\"/3x7 cm. In a giftbox.", full_price="10.00", barcode="8521456987112", product_category_id=3)
# product7 = Product(name="Frodo Keyring", description="3Frodo POP! Keyring Character. Made from vinyl. Dimensions 2.54 x 2.54  x 3.81 cm.", full_price="8.00", barcode="3248561258741", product_category_id=3)
#
# products2 = [product4, product5, product6, product7]
#
# db.session.add_all(products2)
# db.session.commit()


# games category
# product8 = Product(name="The Lord of the Rings Monopoly: Trilogy Edition", description="Chess set made complte with chess pieces, board and storage bags. Board dimensions 47x47x1cm", full_price="75.00", barcode="2547812547842", product_category_id=2)
# product9 = Product(name="Battle for Middle-earth Chess Set", description="Chess set made from plastic and card. Compete with chess pieces, board and storage bags. Board dimensions 47 x 47 x 1 centimetres", full_price="24.99", barcode="3254158749632", product_category_id=2)
# product10 = Product(name="Lord of the Rings Collectible Chess Set - Officially Licensed Film Set Movie Gifts", description="32 precise miniature sculptures crafted in fine pewter of actual cast members. Ancient map of Middle-earth mounted below the playing surface. The base features images of memorable characters and scenes from the trilogy. 15x15\" (38x38cm)", full_price="350.00", barcode="1479652365412", product_category_id=2)
# product11 = Product(name="The Lord of the Rings Playing Cards Standard Deck with Embossed Tin", description="Standard deck of playing cards with a section of the Middle Earth map as a background. Includes an embossed storage tin", full_price="12.00", barcode="5471124552136", product_category_id=2)
# product12 = Product(name="The Magic Hexagon Brain Teaser", description="Form a magic hexagon by joining the moviecards the right way. The box has as a bonus cut-out figures and part of a movie calendar", full_price="15.00", barcode="1224563125133", product_category_id=2)
# product13 = Product(name="Lord of the Rings Heroes of Middle Earth 1000 Piece Jigsaw Puzzle", description="Delve into the world of Lord of the Rings with this beautiful jigsaw puzzle where Aragorn, Éowyn, Gandalf, Sam, Frodo, Legolas and Gimli prepare for battle. 1000 pieces. 35.1 x 27.2 x 5.5 cm", full_price="15.99", barcode="2475113345262", product_category_id=2)
# product14 = Product(name="Gollum delux art figurine", description="Polystone gollum statue. 12 cm tall and comes with matching base.", full_price="19.99", barcode="2470013345269", product_category_id=2, image_id=14)

# db.session.add(products14)
# db.session.commit()

# products3 = [product8, product9, product10, product11, product12, product13]
#
# db.session.add_all(products3)
# db.session.commit()


# # collectibles category
# product14 = Product(name="Lord of the Rings Gimli Figure", description="This Gimli is a 7-inch scale figure featuring 16 points of articulation, detailed sculpting and a full range of accessories. Comes packaged in a full-color window box with hangtag. 6.4 x 5.1 x 15.2cm", full_price="40.00", barcode="5482365121224", available_stock=6, product_category_id=4)
# product15 = Product(name="Lord of the Rings Legolas Action Figure", description="This Legolas is a 7-inch scale figure featuring 16 points of articulation, detailed sculpting and a full range of accessories. Comes packaged in a full-color window box with hangtag.  5.4 x 2.5 x 18.8cm", full_price="40.00", barcode="5911233215521", available_stock=5, product_category_id=4)
# product16 = Product(name="Lord of the Rings Galadriel Figurine", description="This Galadriel figurine is made of lead and painted by hand. Comes boxed with a magazine (in English) about the character in the saga. 30 x 20 x 10cm", full_price="40.00", barcode="1248555112322", available_stock=8, product_category_id=4)
# product17 = Product(name="Lord of the Rings Statue Gollum", description="Tortured and wrought wretched by the lure of the One Ring, Gollum is a withered, piteous creature. The most iconic creature from The Lord Of The Rings movie trilogy, Gollum was also a technological breakthrough. The statue is an Open Edition piece. 14 x 11 x 15cm", full_price="75.00", barcode="3225122445623", available_stock=5, product_category_id=4)
# product18 = Product(name="Elven Green Leaf Brooch Pin Pendant Necklace with Jewellery Box", description="Made from platinum and enamel. Necklace with a metal detailed jewellery box.Pendant Size :6.5*4.5CM Chain Length:50±2CM", full_price="75.00", barcode="2336125446325", available_stock=9, product_category_id=4)
# product19 = Product(name="Lord of the Rings Replica of The One Ring Necklace", description="Ring made for 24 carat gold, with inscription with all round. Box contents: in an jewellery box. Chain 60 cm; Ring Diameter: Approx. 20 mm, scale approx. 62 mm, Width approx. 7 mm", full_price="95.00", barcode="2263255124121", available_stock=12, product_category_id=4)
#
# products4 = [product14, product15, product16, product17, product18, product19]
#
# db.session.add_all(products4)
# db.session.commit()

#attempts to try to alter table with flask_sqlalchemy
from sqlalchemy import update

# from application import db
# from application.models import Customer, Address, RegisteredUser, Product, Size, ProductCategory, Colour, Image
#
# # product images
#
# # img_1 = Image(name='arwen_evenstar_keyring.jpg')
# # db.session.add(img_1)
# # db.session.commit()
#
# # connecting image to product
#
# # image_product_1 = Product(image_id=1)
#
# image_product_1 = Product.query.filter_by(id=2).first()
# image_product_1.image_id = 1
# db.session.commit()
#
# # user = User.query.get(5)
# # user.name = 'New Name'
# # db.session.commit()
#
# # image_product_1 = (
# #     update(Product).
# #     where(Product.id == 2).
# #     values(image_id=1)
# # )
# # db.session.add(image_product_1)
# # db.session.commit()

# # Images
# #
# img1 = Image(name="001.clothes.aragorn.jpg")
# img2 = Image(name="002.keyring.arwen.jpg")
# img3 = Image(name="003.clothes.gandalf.jpg")
# img4 = Image(name="004.keyring.oneringbadge.jpg")
# img5 = Image(name="005.keyring.oneringkeyring.jpg")
# img6 = Image(name="006.keyring.lorienleaf.jpg")
# img7 = Image(name="007.keyring.frodo.jpg")
# img8 = Image(name="008.games.lotrmonopoly.jpg")
# img9 = Image(name="009.games.chessbattle.jpg")
# img10 = Image(name="010.games.chesslotrdeluxe.jpg")
# img11 = Image(name="011.games.lotrcards.jpg")
# img12 = Image(name="012.games.hexagonteaser.jpg")
# img13 = Image(name="013.games.heroes1000p.jpg")
# img14 = Image(name="014.collectibles.gollumfigurine.jpg")
# img15 = Image(name="015.collectibles.gimli.jpg")
# img16 = Image(name="016.collectibles.legolas.jpg")
# img17 = Image(name="017.collectibles.galadriel.jpg")
# img18 = Image(name="018.collectibles.gollum.jpg")
# img19 = Image(name="019.collectibles.elevnleaf.jpg")
# img20 = Image(name="020.collectibles.oneringnecklace.jpg")
# images = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img16, img17,  img18, img19, img20]
# db.session.add_all(images)
# db.session.commit()


# img14 = Image(name="14.collectibles.gollumfigurine.jpg")
# db.session.add(img14)
# db.session.commit()


# images = Image.query.filter_by(id=1)
# print(images)

# products = Product.query.filter_by(id=3)
# for product in products:
#     id = product.id
#     print(product.name,
#           product.description,
#           product.full_price,
#           product.image_id)
#     image = Image.query.filter_by(id=product.image_id)
#     for i in image:
#         print(i.name)
#     products = Product.query.filter_by(id=3)
#     for product in products:
#         id = product.id
#     images = Image.query.filter_by(id=product.image_id)
#     for image in images:
#         image_name = Image.query.filter_by(id=product.image_id)
#         print(image.name)

# product = Product.query.filter_by(id=1).first()
# print(product)


# admin1 = Admin(user_name='admin', email="jihan.alfarra@gmail.com", password="admin", staff_id="1")
# staff1 = Staff(first_name='Jihan', last_name="Alfarra", DOB="1900-11-05", job_title="Web manager", start_date="2022-01-01")

# TESTING SHOPPING CART DICTIONARY
# product_id = 1
# quantity = 1
# product = Product.query.filter_by(id=product_id).first()
# CartItem = {product_id: {'name': product.name, 'price': product.full_price, 'quantity': quantity}}
# # CartItem2 = {product_id: {'name': product.name, 'price': product.full_price, 'quantity': quantity}}
#
# Cart = {}
# Cart = CartItem
# # Cart = Cart + CartItem2
# print(Cart[product_id])
# print(len(Cart))

# staff1 = Staff(first_name='Jihan', last_name="Alfarra", DOB="1900-11-05", job_title="Web manager", start_date="2022-01-01")
# admin1 = Admin(user_name="admin", email="jihan.alfarra@gmail.com", password="admin", staff_id="1")
# db.session.add(admin1)
# db.session.commit()

# ALTER TABLE `lotr_shop`.`customer`
# CHANGE COLUMN `contact_no` `contact_no` VARCHAR(11) NULL ;
#
# ALTER TABLE `lotr_shop`.`customer`
# CHANGE COLUMN `address` `address` INT NULL ;

# customer = RegisteredUser.query.filter_by(email="john@email.com").first()
# customer_id = customer.customer_id

customer_details = Customer.query.filter_by(id=1).first()
first_name = customer_details.first_name
print(first_name)