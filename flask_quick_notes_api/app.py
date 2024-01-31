from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_basicauth import BasicAuth

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'MYSQLusername'
app.config['MYSQL_PASSWORD'] = 'MYSQLpassword'
app.config['MYSQL_DB'] = 'MYSQLdatabasename'

mysql = MySQL(app)

# Basic Authentication Configuration
app.config['BASIC_AUTH_USERNAME'] = 'username' # Placeholder for connecting to POSTMAN
app.config['BASIC_AUTH_PASSWORD'] = 'password' # Placeholder for connecting to POSTMAN
basic_auth = BasicAuth(app)

# Route to get all notes
@app.route('/notes', methods=['GET'])
@basic_auth.required
def get_notes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM notes")
    notes = cur.fetchall()
    cur.close()
    return jsonify({'notes': notes})

# Route to get a specific note by ID
@app.route('/notes/<int:note_id>', methods=['GET'])
@basic_auth.required
def get_note(note_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM notes WHERE id = %s", (note_id,))
    note = cur.fetchone()
    cur.close()
    if note:
        return jsonify({'note': note})
    else:
        return jsonify({'message': 'Note not found'}), 404

# Route to add a new note
@app.route('/notes', methods=['POST'])
@basic_auth.required
def add_note():
    data = request.get_json()
    title = data['title']
    content = data['content']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Note added successfully'})

# Route to update a note by ID
@app.route('/notes/<int:note_id>', methods=['PUT'])
@basic_auth.required
def update_note(note_id):
    data = request.get_json()
    title = data['title']
    content = data['content']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (title, content, note_id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Note updated successfully'})

# Route to delete a note by ID
@app.route('/notes/<int:note_id>', methods=['DELETE'])
@basic_auth.required
def delete_note(note_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Note deleted successfully'})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
