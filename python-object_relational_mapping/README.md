# Python - Object Relational Mapping (ORM)

## Description

This project introduces the connection between Python and MySQL databases using two different approaches:

- **MySQLdb (mysqlclient):** Execute SQL queries directly from Python.
- **SQLAlchemy ORM:** Interact with database tables through Python objects instead of writing raw SQL queries.

The goal is to understand how Python applications communicate with relational databases and how Object Relational Mapping (ORM) simplifies database interactions.

---

## Learning Objectives

By completing this project, I learned how to:

- Connect a Python script to a MySQL database.
- Execute SQL queries from Python using MySQLdb.
- Retrieve and insert data into MySQL tables.
- Understand the concept of Object Relational Mapping (ORM).
- Map Python classes to MySQL tables using SQLAlchemy.
- Build database-driven Python applications following best practices.

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQL 8.0
- MySQLdb (mysqlclient 2.0.x)
- SQLAlchemy 1.4.x
- pycodestyle 2.7.x
- All files executable
- All files end with a new line
- Module, class and function documentation required

---

## Project Structure

```text
python-object_relational_mapping/
├── README.md
├── 0-select_states.py
├── ...
```

---

## Files

| File | Description |
|------|-------------|
| `0-select_states.py` | Lists all states from a MySQL database using MySQLdb. |

---

## Usage

Example:

```bash
./0-select_states.py root root hbtn_0e_0_usa
```

Output:

```text
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

---

## Technologies Used

- Python 3
- MySQL
- MySQLdb (mysqlclient)
- SQLAlchemy
- SQL
- Ubuntu Linux

---

## Author

**Anthony Caban**

Student at Holberton School

GitHub: https://github.com/anthocab2