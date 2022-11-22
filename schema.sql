DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Seller;


CREATE TABLE item (
    itemId INTEGER PRIMARY KEY AUTOINCREMENT,
    itemName  TEXT NOT NULL,
    itemPrice decimal NOT NULL,
    itemDescription text not null,
    itemcatId INTEGER not null,
    itemsellerId INTEGER NOT NULL ,
    image_path VARCHAR not null,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (itemcatId)
       REFERENCES Category (catId) ,
    FOREIGN KEY (itemsellerId)
       REFERENCES seller (sellerId) 
   
);

CREATE TABLE Category (
    catId integer PRIMARY KEY AUTOINCREMENT, 
    category_name VARCHAR,
    category_description TEXT
    
     

);


CREATE TABLE seller (
    sellerId INTEGER PRIMARY KEY AUTOINCREMENT,
    sellerName  TEXT NOT NULL,
    sellerEmail text NOT NULL,
    sellerPassword text not null,
    sellerLocation text not null,
    sellerCountry text not null,
    sellerDescription text not null,
    
    sellercreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP

   
 
   
);
