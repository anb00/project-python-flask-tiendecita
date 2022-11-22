import sqlite3

connection = sqlite3.connect('database-marketplace.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


cur.execute("INSERT INTO seller (sellerName,sellerEmail,sellerPassword,sellerLocation,sellerCountry,sellerDescription,sellercreated) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('JohnSeller', 'johnelectronics@gmail.com','password','New York','USA','I sell electronics for food','')
            )
cur.execute("INSERT INTO seller (sellerName,sellerEmail,sellerPassword,sellerLocation,sellerCountry,sellerDescription,sellercreated) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('MikeSeller', 'Mikefurniture@gmail.com','password','Miami','USA','I sell Furniture','')
            )
cur.execute("INSERT INTO seller (sellerName,sellerEmail,sellerPassword,sellerLocation,sellerCountry,sellerDescription,sellercreated) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('BobSeller', 'Bobmeals@gmail.com','password','Spain','ESP','Take away food','')
            )
cur.execute("INSERT INTO seller (sellerName,sellerEmail,sellerPassword,sellerLocation,sellerCountry,sellerDescription,sellercreated) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('DominicServices', 'servicesDom@gmail.com','password','Texas','USA','Providing services all kind of services','')
            )

cur.execute("INSERT INTO item (itemName,itemPrice,itemDescription,itemcatId,itemsellerId,image_path,created) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('iphoneX', '999','Second hand iphone for sale ,very good conditions',1,1,'imageiphonex.jpg',CURRENT_TIMESTAMP)
            )
cur.execute("INSERT INTO item (itemName,itemPrice,itemDescription,itemcatId,itemsellerId,image_path,created) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('iphoneXII', '1050','Second hand iphone xii for sale ,very good conditions',1,1,'imageiphonexII.jpg','')
            )
cur.execute("INSERT INTO item (itemName,itemPrice,itemDescription,itemcatId,itemsellerId,image_path,created) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Simple Hamburger ', '9','Hamburger with lettude,tomato,onion,ketchup,and delicious beff',3,2,'imagehamburger.jpg','')
            )
cur.execute("INSERT INTO item (itemName,itemPrice,itemDescription,itemcatId,itemsellerId,image_path,created) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Complex Hamburger', '19','Hamburger doble beff,cheese,tomato,onion,lettuce,ketchup',3,2,'imagehamcomplex.jpg','')
            )
cur.execute("INSERT INTO item (itemName,itemPrice,itemDescription,itemcatId,itemsellerId,image_path,created) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Complex Hamburger with Fried potatoes', '999','Hamburger doble beff,cheese,tomato,onion,lettuce,ketchup and potatoes',3,2,'imagehamcomplexpotatoes.jpg','')
            )
cur.execute("INSERT INTO item (itemName,itemPrice,itemDescription,itemcatId,itemsellerId,image_path,created) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Gamming Chair Bultaco  Black', '100','Second hand Gamming Chair Good conditions ',2,3,'imagegammingbultaco.jpg','')
            )
cur.execute("INSERT INTO item (itemName,itemPrice,itemDescription,itemcatId,itemsellerId,image_path,created) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Web Design', '50','Webshop for hire, website for youe business dark net Style',4,3,'imagewebdesign1.jpg','')
            )
cur.execute("INSERT INTO item (itemName,itemPrice,itemDescription,itemcatId,itemsellerId,image_path,created) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('RX 590 Blue', '150','AMD RX ',1,1,'imagex570r.jpg',CURRENT_TIMESTAMP)
            )

cur.execute("INSERT INTO Category (category_name,category_description) VALUES (?, ?)",
            ('Electronics', 'Devices, electronic goods,etc')
            )
cur.execute("INSERT INTO Category (category_name,category_description) VALUES (?, ?)",
            ('Furniture', 'Decotarion,Home Furniture')
            )
cur.execute("INSERT INTO Category (category_name,category_description) VALUES (?, ?)",
            ('Food', 'Meals and Desserts take away')
            )
cur.execute("INSERT INTO Category (category_name,category_description) VALUES (?, ?)",
            ('Services', 'Jobs,services for btc or cash')
            )

connection.commit()
connection.close()