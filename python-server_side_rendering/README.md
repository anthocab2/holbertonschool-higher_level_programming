# Python - Server-Side Rendering

## Description

This project introduces server-side rendering using Python and Flask.

Server-side rendering, also known as SSR, is a technique where HTML pages are generated on the server before being sent to the client's browser. This allows web applications to deliver fully rendered pages, improve search engine optimization, and reduce the amount of processing required on the client side.

Throughout this project, different data sources such as JSON files, CSV files, and SQLite databases are used to generate dynamic HTML content with the Jinja templating engine.

## Learning Objectives

By the end of this project, you should be able to:

* Explain server-side rendering and how it differs from client-side rendering.
* Describe the benefits of server-side rendering.
* Generate dynamic content using Python.
* Implement server-side rendering with Flask.
* Use the Jinja templating engine.
* Read and display data from JSON files.
* Read and display data from CSV files.
* Retrieve and display data from SQLite databases.
* Handle user input and dynamic web content.
* Perform file operations in Python.
* Handle errors and invalid inputs gracefully.

## Requirements

* All files are interpreted or compiled on Ubuntu.
* Python scripts use Python 3.
* Python files must end with a new line.
* The first line of Python executable files must be:

```python
#!/usr/bin/python3
```

* Code should follow the `pycodestyle` style guide.
* All files must be executable when required.
* A `README.md` file must exist in the project directory.

## Project Structure

```text
python-server_side_rendering/
├── README.md
├── task_00_intro.py
└── template.txt
```

## Files

### `task_00_intro.py`

Contains the `generate_invitations` function.

The function receives:

* A string containing an invitation template.
* A list of dictionaries containing attendee information.

For every attendee, the function replaces the following placeholders:

* `{name}`
* `{event_title}`
* `{event_date}`
* `{event_location}`

The generated invitations are saved in sequential files:

```text
output_1.txt
output_2.txt
output_3.txt
```

Missing or `None` values are replaced with:

```text
N/A
```

The function also handles:

* Invalid template types.
* Invalid attendee list types.
* Empty templates.
* Empty attendee lists.
* Missing attendee information.
* File writing errors.

### `template.txt`

Contains the invitation template used by the program:

```text
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
```

## Usage

Import the function from `task_00_intro.py`:

```python
from task_00_intro import generate_invitations
```

Read the template file:

```python
with open("template.txt", "r", encoding="utf-8") as file:
    template_content = file.read()
```

Create the attendee data:

```python
attendees = [
    {
        "name": "Alice",
        "event_title": "Python Conference",
        "event_date": "2023-07-15",
        "event_location": "New York"
    },
    {
        "name": "Bob",
        "event_title": "Data Science Workshop",
        "event_date": "2023-08-20",
        "event_location": "San Francisco"
    },
    {
        "name": "Charlie",
        "event_title": "AI Summit",
        "event_date": None,
        "event_location": "Boston"
    }
]
```

Generate the invitation files:

```python
generate_invitations(template_content, attendees)
```

## Expected Output Files

After running the program, the following files should be generated:

```text
output_1.txt
output_2.txt
output_3.txt
```

Example content of `output_1.txt`:

```text
Hello Alice,

You are invited to the Python Conference on 2023-07-15 at New York.

We look forward to your presence.

Best regards,
Event Team
```

Example content of `output_3.txt`:

```text
Hello Charlie,

You are invited to the AI Summit on N/A at Boston.

We look forward to your presence.

Best regards,
Event Team
```

## Error Handling

### Empty template

```text
Template is empty, no output files generated.
```

### Empty attendee list

```text
No data provided, no output files generated.
```

### Invalid input type

The function displays an error message indicating which input has an invalid type and terminates without creating output files.

### Missing attendee data

Missing keys or values equal to `None` are replaced with:

```text
N/A
```

## Testing

Run the main test file:

```bash
python3 main_00.py
```

List the generated files:

```bash
ls output_*.txt
```

Display an invitation:

```bash
cat output_1.txt
```

Check the Python code style:

```bash
pycodestyle task_00_intro.py
```

## Technologies

* Python 3
* Flask
* Jinja2
* JSON
* CSV
* SQLite
* HTML
* Server-Side Rendering

## Repository

GitHub repository:

```text
holbertonschool-higher_level_programming
```

Project directory:

```text
python-server_side_rendering
```

## Author

**Anthony Caban**