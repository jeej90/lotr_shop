from application import db
from application.models import Customer, Address, RegisteredUser, Product, Size, ProductCategory, Colour

# PRODUCT LIST

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
#
# products3 = [product8, product9, product10, product11, product12, product13]
#
# db.session.add_all(products3)
# db.session.commit()


# collectibles category
# product14 =
# product15 =
# product16 =
# product17 =
# product18 =
# product19 =
#
# products4 = [product14, product15, product16, product17, product18, product19]
#
# db.session.add_all(products4)
# db.session.commit()

product = Product.query.filter_by(id=1).first()
print(product)