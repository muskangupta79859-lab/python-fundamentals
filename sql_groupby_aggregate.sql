-- This file demonstrates aggregate functions with GROUP BY

-- Using existing table: students

-- Count total students
SELECT COUNT(*) FROM students;

-- Average marks of all students
SELECT AVG(marks) FROM students;

-- Maximum and minimum marks
SELECT MAX(marks), MIN(marks) FROM students;

-- Average marks per course
SELECT course, AVG(marks)
FROM students
GROUP BY course;

-- Total students per course
SELECT course, COUNT(*)
FROM students
GROUP BY course;

-- Courses with average marks greater than 75
SELECT course, AVG(marks)
FROM students
GROUP BY course
HAVING AVG(marks) > 75;
