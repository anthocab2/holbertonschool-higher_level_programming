# Python Serialization

## Description

This project introduces the concepts of serialization and deserialization in Python.

Serialization is the process of converting Python objects into a format that can be stored or transmitted. Deserialization is the reverse process, where serialized data is converted back into Python objects.

The project focuses on working with JSON and other serialization techniques commonly used in software development, APIs, databases, and distributed systems.

---

## Learning Objectives

At the end of this project, I am able to explain:

* The difference between marshaling and serialization
* How to serialize Python objects
* How to deserialize data back into Python objects
* How JSON is used for data exchange
* How serialization is used in APIs and network communication
* The advantages and limitations of different serialization formats

---

## Requirements

* Ubuntu 22.04 LTS
* Python 3.10.*
* pycodestyle 2.7.*
* All files executable
* All files end with a new line
* Documentation for modules and functions

---

## Project Structure

| File                           | Description                                              |
| ------------------------------ | -------------------------------------------------------- |
| task_00_basic_serialization.py | Serialize and deserialize Python dictionaries using JSON |

---

## Usage

Example:

```python
from task_00_basic_serialization import (
    serialize_and_save_to_file,
    load_and_deserialize
)

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data, "data.json")

loaded_data = load_and_deserialize("data.json")

print(loaded_data)
```

Output:

```python
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```

---

## Author

**Anthony Caban**

Student at Holberton School

GitHub: anthocab2
