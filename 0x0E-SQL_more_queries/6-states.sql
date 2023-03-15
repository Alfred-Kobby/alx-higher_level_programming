-- Create a database and user
-- DDL query to create an user with specific privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Creates the table unique_id.
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id`   INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);
