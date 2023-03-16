-- creates the MySQL server user user_0d_1.
create user 'user_0d_1'@'localhost' IF NOT EXISTS IDENTIFIED WITH authentication_plugin BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'