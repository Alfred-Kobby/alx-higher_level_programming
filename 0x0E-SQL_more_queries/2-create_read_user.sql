-- Creates database htbn_0d2.
CREATE DATABASE
    IF NOT EXISTS 'hbtn_0d_2';
-- Create user to user_0d_2
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
-- add privileges to user
GRANT SELECT PRIVILEGES
   ON 'hbtn_0d_2'.*
   TO 'user_0d_2'@'localhost'
   IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;