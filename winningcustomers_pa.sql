USE JunwenQiu1162541$winningcustomers;
CREATE TABLE customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    prize VARCHAR(100) NOT NULL
);
INSERT INTO customers(name,email,prize)VALUES
('tom','222@gmail.com','switch'),
('john','yyy@qq.com','ps4');
