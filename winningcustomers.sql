USE winning customers;
CREATE TABLE customers(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
	email VARCHAR(100)
	prize VARCHAR(100)
);
INSERT INTO customers(name,email,prize)
VALUES
('tom','222@gmail.com','switch')
('john','yyy@qq.com','ps4')