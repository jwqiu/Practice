USE JunwenQiu1162541$library;
CREATE TABLE wiinningcustomers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    prize VARCHAR(100) NOT NULL
);
INSERT INTO wiinningcustomers(name,email,prize)VALUES
('tom','222@gmail.com','switch')
('john','yyy@qq.com','ps4')
