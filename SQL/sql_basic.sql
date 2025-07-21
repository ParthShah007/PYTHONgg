vcreate table products(
product_id serial primary key,
name varchar(60) not null,
sku_code char(8) unique not null,
price numeric(10,2) default 0 check (price >= 0),
stock_quantity int default 0 check (stock_quantity >= 0),
is_available boolean default TRUE,
category text not null,
added_on date default current_date,
last_update Timestamp default now()
);

insert into products(name, sku_code, price, stock_quantity, is_available, category)
values
('Wireless Mouse', 101, 1611.53, 79, FALSE, 'Electronics'),
('Bluetooth Speaker', 102, 135.14, 23, TRUE, 'Electronics'),
('Laptop Stand', 103, 1020.92, 161, FALSE, 'Accessories'),
('USB-C Hub', 104, 408.39, 164, FALSE, 'Accessories'),
('Notebook', 105, 1987.74, 116, TRUE, 'Stationery'),
('Pen Set', 106, 1048.10, 150, TRUE, 'Stationery'),
('Coffee Mug', 107, 1063.53, 76, FALSE, 'Home & Kitchen'),
('LED Desk Lamp', 108, 239.10, 93, FALSE, 'Home & Kitchen'),
('Yoga Mat', 109, 1514.86, 162, TRUE, 'Fitness'),
('Water Bottle', 110, 420.99, 191, TRUE, 'Fitness'),
('Smartphone', 111, 361.20, 200, FALSE, 'Electronics'),
('Headphones', 112, 154.84, 178, TRUE, 'Electronics'),
('Gaming Keyboard', 113, 103.24, 100, FALSE, 'Accessories'),
('Monitor', 114, 305.20, 123, FALSE, 'Electronics'),
('HDMI Cable', 115, 552.97, 105, TRUE, 'Accessories'),
('Power Bank', 116, 831.88, 13, FALSE, 'Electronics'),
('Backpack', 117, 1517.11, 64, TRUE, 'Accessories'),
('Webcam', 118, 1428.30, 76, FALSE, 'Electronics'),
('Desk Organizer', 119, 404.69, 136, FALSE, 'Home & Kitchen'),
('Fitness Band', 120, 1451.69, 171, FALSE, 'Fitness');

select * from products;