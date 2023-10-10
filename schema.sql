DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    country TEXT NOT NULL
);

DROP TABLE IF EXISTS doctor_departments;
CREATE TABLE doctor_departments (
        id INTEGER NOT NULL,
        name VARCHAR(255),
        details VARCHAR(255),
        PRIMARY KEY (id)
)


DROP TABLE IF EXISTS doctors;
CREATE TABLE doctors (
        id INTEGER NOT NULL,
        name VARCHAR(255),
        title VARCHAR(255),
        department VARCHAR(255),
        phone VARCHAR(255),
        details VARCHAR(255),
        PRIMARY KEY (id)
)


DROP TABLE IF EXISTS patients;
CREATE TABLE patients (
        id INTEGER NOT NULL,
        name VARCHAR(255),
        phone VARCHAR(255),
        address VARCHAR(255),
        doctor VARCHAR(255),
        serial_number VARCHAR(255),
        booked_or_visited BOOLEAN,
        PRIMARY KEY (id)
)