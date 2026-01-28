-- This file demonstrates JOIN operations with proper table creation and data

-- Create Database
CREATE DATABASE college_db;
USE college_db;

-- Create Tables

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert Data into Courses Table
INSERT INTO courses VALUES
(1, 'Data Science'),
(2, 'Computer Science'),
(3, 'Artificial Intelligence');

-- Insert Data into Students Table
INSERT INTO students VALUES
(101, 'Aman', 1),
(102, 'Riya', 2),
(103, 'Kunal', 1),
(104, 'Neha', NULL);

-- View Tables
SELECT * FROM courses;
SELECT * FROM students;

-- INNER JOIN
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.course_id;

-- LEFT JOIN
SELECT students.name, courses.course_name
FROM students
LEFT JOIN courses
ON students.course_id = courses.course_id;

-- RIGHT JOIN
SELECT students.name, courses.course_name
FROM students
RIGHT JOIN courses
ON students.course_id = courses.course_id;
