CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
/*
 The code above make it so that if the table does not already exist it will create the table
 It will also make sure that the username and password are entered as it is mandatory
 */