-- SQL Basics 

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    age INTEGER,
    marks INTEGER
);

INSERT INTO students VALUES (1, 'Amit', 20, 85);
INSERT INTO students VALUES (2, 'Neha', 21, 90);
INSERT INTO students VALUES (3, 'Rahul', 19, 78);

SELECT * FROM students;
SELECT name, marks FROM students WHERE marks > 80;

UPDATE students
SET marks = 88
WHERE id = 3;

DELETE FROM students WHERE id = 1;
