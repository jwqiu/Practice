-- 切换到目标数据库
USE JunwenQiu1162541$library;

-- 创建一个简单的表
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY, -- 自增主键
    title VARCHAR(100) NOT NULL,       -- 书名
    author VARCHAR(100) NOT NULL,      -- 作者
    published_year INT                  -- 出版年份
);

-- 向表中插入一些示例数据
INSERT INTO books (title, author, published_year) VALUES
('To Kill a Mockingbird', 'Harper Lee', 1960),
('1984', 'George Orwell', 1949),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925);