-- SQL SELECT and Conditions Practice

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    age INTEGER,
    marks INTEGER,
    city TEXT
);

INSERT INTO students VALUES (1, 'Amit', 20, 85, 'Delhi');
INSERT INTO students VALUES (2, 'Neha', 21, 90, 'Lucknow');
INSERT INTO students VALUES (3, 'Rahul', 19, 78, 'Kanpur');
INSERT INTO students VALUES (4, 'Pooja', 22, 92, 'Delhi');

-- Select all data
SELECT * FROM students;

-- Select specific columns
SELECT name, marks FROM students;

-- Use WHERE condition
SELECT * FROM students WHERE city = 'Delhi';

-- Use AND condition
SELECT * FROM students WHERE marks > 80 AND age > 20;

-- Order data
SELECT * FROM students ORDER BY marks DESC;

-- Limit records
SELECT * FROM students ORDER BY marks DESC LIMIT 2;
