# Flask Note Taking API

This is a simple Flask API for note-taking, providing basic CRUD (Create, Read, Update, Delete) operations. The API uses MySQL for data storage and implements Basic Authentication for secure access.

## Features

- **Get all notes:** Retrieve a list of all notes.
- **Get a specific note by ID:** Fetch details of a note using its unique identifier.
- **Add a new note:** Create a new note with a title and content.
- **Update a note by ID:** Modify the title or content of an existing note.
- **Delete a note by ID:** Remove a note from the database.

## Technologies Used

- **Flask:** A micro web framework for Python.
- **Flask-MySQLdb:** Flask extension for MySQL integration.
- **Flask-BasicAuth:** Flask extension for basic HTTP authentication.

## Setup Instructions

1. Clone the repository.
2. Set up a virtual environment and install dependencies.
3. Configure MySQL database details in the app.py file.
4. Activate the virtual environment.
5. Run the Flask application with `python app.py`.
6. Use Postman or any API testing tool to interact with the endpoints.

## API Endpoints

- **GET /notes:** Retrieve all notes.
- **GET /notes/{note_id}:** Retrieve details of a specific note.
- **POST /notes:** Create a new note.
- **PUT /notes/{note_id}:** Update an existing note.
- **DELETE /notes/{note_id}:** Delete a note.

## Sample Request (Postman)

### POST /notes

- **URL:** `http://127.0.0.1:5000/notes`
- **Method:** POST
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Basic base64(username:password)`
- **Body:**

```json
{
  "title": "Sample Note",
  "content": "This is a sample note content."
}


