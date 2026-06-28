# SQL Introduction

## Description

This project is part of the Holberton School Higher Level Programming curriculum.

The goal of this project is to learn the fundamentals of relational databases and SQL using MySQL 8. Students will create SQL scripts to manipulate databases, tables, and data while following SQL best practices.

---

## Learning Objectives

By the end of this project, I should be able to explain:

- What a database is
- What a relational database is
- What SQL stands for
- What MySQL is
- How to create databases
- How to create and modify tables
- The difference between DDL and DML
- How to retrieve data using SELECT
- How to insert, update and delete data
- How to write subqueries
- How to use SQL functions

---

## Requirements

- Ubuntu 22.04 LTS
- MySQL 8.0
- Allowed editors:
  - vi
  - vim
  - emacs
- Every SQL file starts with a task description comment.
- Every SQL query has a comment immediately before it.
- All SQL keywords are written in uppercase.
- Every file ends with a new line.

---

## Project Structure

| File | Description |
|------|-------------|
| `0-list_databases.sql` | Lists all databases on the MySQL server. |

---

## Usage

Run a SQL script using:

```bash
cat filename.sql | mysql -hlocalhost -uroot -p
```

Example:

```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

---

## Author

**Anthony Caban**

Student at Holberton School.