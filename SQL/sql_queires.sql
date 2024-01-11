-- Create a table of users and perform database queries.

-- get values of specific columns
SELECT `first_name`,`email` FROM `users`;

-- get value of all columns
SELECT * FROM `users` ;

-- get values with where clause
SELECT *  FROM `users` WHERE `email` = 'admin@admin.com';

-- get values by id
SELECT *  FROM `users` WHERE `id` = 23;

-- get specific columns of desired id
SELECT `name`,`email`,`password` FROM `users` WHERE `id` = 23;

-- AND example
SELECT `name`,`email`,`password` FROM `users` WHERE `email` = 'admin@admin.com' AND `id` = 2;

-- OR example
SELECT `name`,`email`,`password` FROM `users` WHERE `email` = 'admin@admin.com' OR `id` = 23;

-- insert a new record
INSERT INTO `users` 
VALUES (1,  'Ahmad', 'Abdullah', 'adhmadabdullah@gmail.com', '+9230012345678');

-- inset new record with columns name
INSERT INTO `users` (`phone`,`fname`,`lname`,`email`)
VALUES ('13156564654325','Ahmad','ahsan', 'adhmadahsan@gmail.com');

-- upadate specific row in table
UPDATE `users`  
SET `phone` = '0300123456789'
WHERE `id` = 1;

-- second example
UPDATE `users`
SET `phone` = '0200123456789'
WHERE `email` = 'adhmadahsan@gmail.com';

-- Delete row
DELETE FROM `users` WHERE `id` = 5;
DELETE FROM `users` WHERE `id` IN (68,71,75,53,60);